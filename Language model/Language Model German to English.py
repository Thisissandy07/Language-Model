import tkinter as tk
from tkinter import ttk, messagebox
from huggingface_hub import InferenceClient
import os
TRANSLATION_MODELS = {
    ("German", "English"): "Helsinki-NLP/opus-mt-de-en",
    ("English", "German"): "Helsinki-NLP/opus-mt-en-de",
    ("French", "English"): "Helsinki-NLP/opus-mt-fr-en",
    ("English", "French"): "Helsinki-NLP/opus-mt-en-fr",
    ("Spanish", "English"): "Helsinki-NLP/opus-mt-es-en",
    ("English", "Spanish"): "Helsinki-NLP/opus-mt-en-es",
}


LANGUAGES = sorted(set(lang for pair in TRANSLATION_MODELS.keys() for lang in pair))

client = InferenceClient(
    provider="hf-inference",
    token= "Enter Token Value"
)

def translate_text():
    src = source_lang.get()
    tgt = target_lang.get()

    if src == tgt:
        messagebox.showwarning("Language Error", "Source and target languages must be different.")
        return
    model = TRANSLATION_MODELS.get((src, tgt))
    if not model:
        messagebox.showerror(
            "Model Missing",
            f"No model available for {src} → {tgt}"
        )
        return

    text = input_text.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Input Error", "Please enter text to translate.")
        return
    try:
        result = client.translation(text, model=model)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, result["translation_text"])
    except Exception as e:
        messagebox.showerror("Translation Error", str(e))
def swap_languages():
    s = source_lang.get()
    t = target_lang.get()

    source_lang.set(t)
    target_lang.set(s)


root = tk.Tk()
root.title("Multi-Language Translator")
root.geometry("700x450")


tk.Label(root, text="Source Language").pack()
source_lang = tk.StringVar(value=LANGUAGES[0])
source_menu = ttk.Combobox(root,
                           textvariable=source_lang, 
                           values=list(LANGUAGES), 
                           width=30)
source_menu.pack()                        

tk.Label(root, text="Target Language").pack()
target_lang = tk.StringVar(value=LANGUAGES[1])
target_menu = ttk.Combobox(root,
                           textvariable=target_lang, 
                           values=list(LANGUAGES), 
                           width=30)
target_menu.pack()

tk.Button(
    root,
    text="↔ Swap Languages",
    font=("Arial", 10, "bold"),
    command=swap_languages
).pack(pady=5)

tk.Label(root, text="Enter Text").pack()
input_text = tk.Text(root, height=6, width=60)
input_text.pack()



tk.Label(root, text="Translated Text").pack()
output_text = tk.Text(root, height=6, width=60, bg="#f0f0f0")
output_text.pack()
tk.Button(root, text="Translate", command=translate_text).pack()

root.mainloop()










