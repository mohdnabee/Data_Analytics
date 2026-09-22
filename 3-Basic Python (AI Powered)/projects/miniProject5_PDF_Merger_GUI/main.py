import tkinter as tk
from tkinter import filedialog, messagebox, ttk

from pypdf import PdfWriter


class PdfMergerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Merger")
        self.root.geometry("620x420")
        self.root.minsize(520, 340)

        self.pdfs = []
        self.output_path = tk.StringVar(value="merged.pdf")

        self._build_ui()

    def _build_ui(self):
        main = ttk.Frame(self.root, padding=16)
        main.pack(fill="both", expand=True)

        ttk.Label(main, text="PDF Merger", font=("Segoe UI", 18, "bold")).pack(
            anchor="w"
        )
        ttk.Label(main, text="Choose PDFs and arrange them in the order they should be merged.").pack(
            anchor="w", pady=(4, 12)
        )

        file_frame = ttk.Frame(main)
        file_frame.pack(fill="both", expand=True)

        self.file_list = tk.Listbox(file_frame, selectmode=tk.SINGLE, height=12)
        self.file_list.pack(side="left", fill="both", expand=True)
        scrollbar = ttk.Scrollbar(file_frame, orient="vertical", command=self.file_list.yview)
        scrollbar.pack(side="left", fill="y")
        self.file_list.configure(yscrollcommand=scrollbar.set)

        controls = ttk.Frame(file_frame, padding=(10, 0, 0, 0))
        controls.pack(side="left", fill="y")
        ttk.Button(controls, text="Add PDFs", command=self.add_pdfs).pack(fill="x", pady=(0, 6))
        ttk.Button(controls, text="Remove", command=self.remove_pdf).pack(fill="x", pady=6)
        ttk.Button(controls, text="Move up", command=self.move_up).pack(fill="x", pady=6)
        ttk.Button(controls, text="Move down", command=self.move_down).pack(fill="x", pady=6)

        output_frame = ttk.Frame(main)
        output_frame.pack(fill="x", pady=(14, 0))
        ttk.Label(output_frame, text="Save as:").pack(side="left")
        ttk.Entry(output_frame, textvariable=self.output_path).pack(
            side="left", fill="x", expand=True, padx=(8, 8)
        )
        ttk.Button(output_frame, text="Browse", command=self.choose_output).pack(side="left")

        ttk.Button(main, text="Merge PDFs", command=self.merge_pdfs).pack(
            anchor="e", pady=(14, 0)
        )

    def add_pdfs(self):
        selected = filedialog.askopenfilenames(
            title="Select PDF files", filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
        )
        for path in selected:
            if path not in self.pdfs:
                self.pdfs.append(path)
                self.file_list.insert(tk.END, path)

    def remove_pdf(self):
        selection = self.file_list.curselection()
        if selection:
            index = selection[0]
            self.file_list.delete(index)
            self.pdfs.pop(index)

    def move_up(self):
        selection = self.file_list.curselection()
        if selection and selection[0] > 0:
            index = selection[0]
            self.pdfs[index - 1], self.pdfs[index] = self.pdfs[index], self.pdfs[index - 1]
            self._refresh_list(index - 1)

    def move_down(self):
        selection = self.file_list.curselection()
        if selection and selection[0] < len(self.pdfs) - 1:
            index = selection[0]
            self.pdfs[index], self.pdfs[index + 1] = self.pdfs[index + 1], self.pdfs[index]
            self._refresh_list(index + 1)

    def _refresh_list(self, selected_index):
        self.file_list.delete(0, tk.END)
        for path in self.pdfs:
            self.file_list.insert(tk.END, path)
        self.file_list.selection_set(selected_index)
        self.file_list.activate(selected_index)

    def choose_output(self):
        path = filedialog.asksaveasfilename(
            title="Save merged PDF",
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")],
            initialfile="merged.pdf",
        )
        if path:
            self.output_path.set(path)

    def merge_pdfs(self):
        output_path = self.output_path.get().strip()
        if not self.pdfs:
            messagebox.showwarning("No PDFs selected", "Add at least one PDF before merging.")
            return
        if not output_path:
            messagebox.showwarning("Missing output file", "Choose a name for the merged PDF.")
            return

        try:
            merger = PdfWriter()
            for pdf in self.pdfs:
                merger.append(pdf)
            with open(output_path, "wb") as output_file:
                merger.write(output_file)
            messagebox.showinfo("Merge complete", f"Saved merged PDF to:\n{output_path}")
        except Exception as error:
            messagebox.showerror("Merge failed", str(error))


if __name__ == "__main__":
    root = tk.Tk()
    PdfMergerApp(root)
    root.mainloop()