import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector as mysql
from dataclasses import dataclass
from typing import List, Dict, Any
import customtkinter as ctk
from PIL import Image, ImageTk
import uuid
try:
    import tkcalendar as tkc
except ImportError:
    tkc = None

# Veritabanı bağlantısı (değişmedi)
def connect_db():
    try:
        return mysql.connect(
            host="localhost",
            user="root",
            password="15082005",
            database="yemek_tarifleri"
        )
    except mysql.Error as e:
        messagebox.showerror("Hata", f"Veritabanı bağlantısı başarısız: {e}")
        return None

# Veritabanı tablolarını oluştur (değişmedi)
def create_tables():
    db = connect_db()
    if db is None:
        return
    cursor = db.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            password VARCHAR(50) NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS recipes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(100) NOT NULL,
            ingredients TEXT NOT NULL,
            content TEXT NOT NULL,
            user_id INT,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ratings (
            id INT AUTO_INCREMENT PRIMARY KEY,
            recipe_id INT,
            rating INT NOT NULL,
            FOREIGN KEY (recipe_id) REFERENCES recipes(id)
        )
    """)
    db.commit()
    cursor.close()
    db.close()

# Görsel ve ikon ayarları (değişmedi)
background_images = {
    "main": "bg.png",
}

icon_images = {
    "add": "add_icon.png",
    "search": "search_icon.png",
    "rate": "rate_icon.png",
    "user": "user_icon.png",
    "ingredient": "ingredient_icon.png",
    "save": "save_icon.png"
}

def set_background(window, image_key, width, height):
    try:
        image_path = background_images.get(image_key, "recipe_bg.png")
        image = Image.open(image_path)
        image = image.resize((width, height), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        background_label = tk.Label(window, image=photo)
        background_label.image = photo
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        background_label.lower()
    except Exception as e:
        print(f"Arka plan görseli yüklenemedi ({image_key}): {e}")

def load_icon(icon_key, size=(20, 20)):
    try:
        image_path = icon_images.get(icon_key, "default_icon.png")
        image = Image.open(image_path)
        image = image.resize(size, Image.Resampling.LANCZOS)
        return ctk.CTkImage(light_image=image, dark_image=image, size=size)
    except FileNotFoundError:
        print(f"İkon dosyası bulunamadı ({icon_key}): {image_path}")
        return None
    except Exception as e:
        print(f"İkon yüklenemedi ({icon_key}): {e}")
        return None

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

# LoginScreen sınıfı (değişmedi, sadece ilgili kısmı atlıyorum)
class LoginScreen:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Zehra'nın Mutfağı - Giriş")
        center_window(self.root, 400, 350)
        self.root.resizable(False, False)
        create_tables()

        ctk.CTkLabel(self.root, text="Kullanıcı Adı:", font=("Arial", 12), fg_color="transparent").pack(pady=10)
        self.entry_username = ctk.CTkEntry(self.root, width=200)
        self.entry_username.pack(pady=5)

        ctk.CTkLabel(self.root, text="Şifre:", font=("Arial", 12), fg_color="transparent").pack(pady=10)
        self.entry_password = ctk.CTkEntry(self.root, show="*", width=200)
        self.entry_password.pack(pady=5)

        ctk.CTkButton(
            self.root,
            text="Giriş Yap",
            command=self.login,
            image=load_icon("user"),
            compound="left",
            width=200,
            font=("Arial", 12, "bold"),
            fg_color="#9bad82",
            bg_color='#242424',
            hover_color="#52603f"
        ).pack(pady=10)

        ctk.CTkButton(
            self.root,
            text="Kayıt Ol",
            command=self.open_register,
            image=load_icon("user"),
            compound="left",
            width=200,
            font=("Arial", 12, "bold"),
            fg_color="#9bad82",
            bg_color='#242424',
            hover_color="#52603f"
        ).pack(pady=10)

        self.root.mainloop()

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        db = connect_db()
        if db is None:
            return
        cursor = db.cursor()
        cursor.execute("SELECT id FROM users WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()
        cursor.close()
        db.close()

        if user:
            self.root.update()
            self.root.quit()
            self.root.destroy()
            import time
            time.sleep(0.1)
            YemekTarifiUygulamasi(user_id=user[0])
        else:
            messagebox.showerror("Hata", "Kullanıcı adı veya şifre yanlış.")

    def open_register(self):
        self.register_window = ctk.CTkToplevel(self.root)
        self.register_window.title("Kayıt Ol")
        center_window(self.register_window, 300, 250)
        self.register_window.resizable(False, False)
        self.register_window.attributes('-topmost', True)

        ctk.CTkLabel(self.register_window, text="Kullanıcı Adı:", font=("Arial", 12), fg_color="transparent").pack(pady=10)
        self.reg_entry_username = ctk.CTkEntry(self.register_window, width=200)
        self.reg_entry_username.pack(pady=5)

        ctk.CTkLabel(self.register_window, text="Şifre:", font=("Arial", 12), fg_color="transparent").pack(pady=10)
        self.reg_entry_password = ctk.CTkEntry(self.register_window, show="*", width=200)
        self.reg_entry_password.pack(pady=5)

        ctk.CTkButton(
            self.register_window,
            text="Kayıt Ol",
            command=self.register,
            image=load_icon("save"),
            compound="left",
            width=200,
            font=("Arial", 12, "bold"),
            fg_color="transparent",
            hover_color="#2F4F4F"
        ).pack(pady=10)

    def register(self):
        username = self.reg_entry_username.get()
        password = self.reg_entry_password.get()

        if not username or not password:
            messagebox.showerror("Hata", "Kullanıcı adı ve şifre boş olamaz!")
            return

        db = connect_db()
        if db is None:
            return
        cursor = db.cursor()
        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            db.commit()
            messagebox.showinfo("Başarılı", "Kayıt tamamlandı!")
            self.register_window.destroy()
        except mysql.Error as e:
            messagebox.showerror("Hata", f"Kayıt başarısız: {e}")
        finally:
            cursor.close()
            db.close()

class YemekTarifiUygulamasi:
    def __init__(self, user_id):
        self.user_id = user_id
        self.pencere = ctk.CTk()
        self.setup_ui()
        self.pencere.mainloop()

    def setup_ui(self):
        self.pencere.title("Zehra'nın Mutfağı")
        center_window(self.pencere, 950, 600)
        self.pencere.resizable(False, False)
        set_background(self.pencere, "main", 950, 600)

        self.create_menu()

        ctk.CTkLabel(
            self.pencere,
            text="",
            fg_color="transparent",
            bg_color='transparent',
        ).grid(row=0, column=0, columnspan=5, pady=40)
        self.create_main_buttons()

    def create_menu(self):
        menu_frame = ctk.CTkFrame(self.pencere, fg_color="transparent", bg_color='#52603f')
        menu_frame.grid(row=0, column=0, sticky="nw", columnspan=5, padx=10)

        self.yardim_var = tk.StringVar(value="Yardım")
        yardim_menu = ctk.CTkOptionMenu(
            menu_frame,
            values=["Nasıl çalışır", "Hakkında", "Çıkış"],
            variable=self.yardim_var,
            command=self.yardim_menu_command,
            width=120,
            font=("Arial", 12),
            fg_color="#333333",
            bg_color='#52603f',
            button_color="#333333",
            button_hover_color="#2F4F4F",
            dropdown_fg_color="#333333"
        )
        yardim_menu.grid(row=0, column=0, padx=5)

        self.tarif_var = tk.StringVar(value="Tarif İşlemleri")
        tarif_menu = ctk.CTkOptionMenu(
            menu_frame,
            values=["Tarif Ekle", "Tarif Ara"],
            variable=self.tarif_var,
            command=self.tarif_menu_command,
            width=120,
            font=("Arial", 12),
            fg_color="#333333",
            bg_color='#52603f',
            button_color="#333333",
            button_hover_color="#2F4F4F",
            dropdown_fg_color="#333333"
        )
        tarif_menu.grid(row=0, column=1, padx=5)

    def yardim_menu_command(self, choice):
        if choice == "Nasıl çalışır":
            self.help_page()
        elif choice == "Hakkında":
            self.about_page()
        elif choice == "Çıkış":
            self.pencere.quit()
        self.yardim_var.set("Yardım")

    def tarif_menu_command(self, choice):
        if choice == "Tarif Ekle":
            self.tarif_ekle_ekrani()
        elif choice == "Tarif Ara":
            self.tarif_ara_ekrani()
        self.tarif_var.set("Tarif İşlemleri")

    def create_main_buttons(self):
        btn_info = [
            ("Tarif Ekle", self.tarif_ekle_ekrani, "add"),
            ("Tarif Ara", self.tarif_ara_ekrani, "search"),
            ("Tarif Değerlendir", self.tarif_degerlendir_ekrani, "rate"),
            ("Malzeme Listesi", self.malzeme_listesi_ekrani, "ingredient"),
            ("Kullanıcı Profili", self.kullanici_profili_ekrani, "user")
        ]
        for idx, (text, command, icon) in enumerate(btn_info):
            ctk.CTkButton(
                self.pencere,
                text=text,
                command=command,
                image=load_icon(icon),
                compound="left",
                font=("Arial", 12, "bold"),
                width=160,
                height=100,
                corner_radius=10,
                fg_color="#9bad82",
                bg_color='#52603f',
                hover_color="#2F4F4F"
            ).grid(row=10, column=idx, pady=120, padx=15)

    def tarif_ekle_ekrani(self):
        self.tarif_ekle_pencere = ctk.CTkToplevel(self.pencere)
        self.tarif_ekle_pencere.title("Tarif Ekle")
        self.tarif_ekle_pencere.resizable(False, False)
        center_window(self.tarif_ekle_pencere, 600, 600)
        self.tarif_ekle_pencere.attributes('-topmost', True)

        labels = ["Tarif Adı", "Malzemeler (her satıra bir malzeme)", "Tarif İçeriği"]
        self.tarif_entries = {}
        for idx, label in enumerate(labels):
            ctk.CTkLabel(
                self.tarif_ekle_pencere,
                text=f"{label}:",
                font=("Arial", 12, "bold"),
                fg_color="transparent"
            ).grid(row=idx + 1, column=0, padx=20, pady=8, sticky="e")
            if label == "Tarif İçeriği":
                entry = ctk.CTkTextbox(self.tarif_ekle_pencere, width=300, height=200)
            elif label == "Malzemeler (her satıra bir malzeme)":
                entry = ctk.CTkTextbox(self.tarif_ekle_pencere, width=300, height=100)
            else:
                entry = ctk.CTkEntry(self.tarif_ekle_pencere, width=300)
            entry.grid(row=idx + 1, column=1, pady=8)
            self.tarif_entries[label] = entry

        ctk.CTkButton(
            self.tarif_ekle_pencere,
            text="Tarif Ekle",
            command=self.tarif_ekle,
            image=load_icon("add"),
            compound="left",
            font=("Arial", 12, "bold"),
            width=300,
            corner_radius=10,
            fg_color="#9bad82",
            hover_color="#52603f"
        ).grid(row=len(labels) + 2, column=0, columnspan=2, pady=20)

    def tarif_ekle(self):
        data = {}
        for k, v in self.tarif_entries.items():
            if isinstance(v, ctk.CTkTextbox):
                text = v.get("1.0", tk.END).strip()
                if k == "Malzemeler (her satıra bir malzeme)":
                    text = ", ".join(line.strip() for line in text.split("\n") if line.strip())
                data[k] = text
            else:
                data[k] = v.get().strip()

        if not all(data.values()):
            messagebox.showerror("Hata", "Tüm alanları doldurun!")
            return

        db = connect_db()
        if db is None:
            return
        cursor = db.cursor()
        try:
            cursor.execute(
                "INSERT INTO recipes (title, ingredients, content, user_id) VALUES (%s, %s, %s, %s)",
                (data["Tarif Adı"], data["Malzemeler (her satıra bir malzeme)"], data["Tarif İçeriği"], self.user_id)
            )
            db.commit()
            messagebox.showinfo("Başarılı", "Tarif başarıyla eklendi!")
            for k, v in self.tarif_entries.items():
                if isinstance(v, ctk.CTkTextbox):
                    v.delete("1.0", tk.END)
                else:
                    v.delete(0, tk.END)
            self.tarif_ekle_pencere.destroy()
        except mysql.Error as e:
            messagebox.showerror("Hata", f"Tarif eklenirken bir hata oluştu: {e}")
        finally:
            cursor.close()
            db.close()

    def tarif_ara_ekrani(self):
        self.tarif_ara_pencere = ctk.CTkToplevel(self.pencere)
        self.tarif_ara_pencere.title("Tarif Ara")
        self.tarif_ara_pencere.resizable(False, False)
        center_window(self.tarif_ara_pencere, 400, 400)
        self.tarif_ara_pencere.attributes('-topmost', True)

        ctk.CTkLabel(
            self.tarif_ara_pencere,
            text="Aranacak Tarif Adı:",
            font=("Arial", 12, "bold"),
            fg_color="transparent"
        ).pack(pady=10)
        self.arama_entry = ctk.CTkEntry(self.tarif_ara_pencere, width=200)
        self.arama_entry.pack(pady=5)

        ctk.CTkButton(
            self.tarif_ara_pencere,
            text="Tarif Ara",
            command=self.tarif_ara,
            image=load_icon("search"),
            compound="left",
            width=200,
            font=("Arial", 12, "bold"),
            fg_color="#9bad82",
            hover_color="#52603f"
        ).pack(pady=10)

        self.sonuc_listbox = tk.Listbox(self.tarif_ara_pencere, width=50, height=10, font=("Arial", 10))
        self.sonuc_listbox.pack(pady=10)
        self.sonuc_listbox.bind('<<ListboxSelect>>', self.show_recipe_details)

    def tarif_ara(self):
        arama_terimi = self.arama_entry.get().lower()
        db = connect_db()
        if db is None:
            return
        cursor = db.cursor()
        try:
            cursor.execute("SELECT id, title FROM recipes WHERE LOWER(title) LIKE %s", (f"%{arama_terimi}%",))
            self.search_results = cursor.fetchall()
            self.sonuc_listbox.delete(0, tk.END)
            if self.search_results:
                for recipe in self.search_results:
                    self.sonuc_listbox.insert(tk.END, recipe[1])
            else:
                self.sonuc_listbox.insert(tk.END, "Aranan tarif bulunamadı.")
        except mysql.Error as e:
            messagebox.showerror("Hata", f"Veri okuma hatası: {e}")
        finally:
            cursor.close()
            db.close()

    def show_recipe_details(self, event):
        selection = self.sonuc_listbox.curselection()
        if not selection:
            return

        recipe_id = self.search_results[selection[0]][0]
        db = connect_db()
        if db is None:
            return
        cursor = db.cursor()
        try:
            cursor.execute("SELECT title, ingredients, content FROM recipes WHERE id = %s", (recipe_id,))
            recipe = cursor.fetchone()
            if recipe:
                self.display_recipe_window(recipe)
        except mysql.Error as e:
            messagebox.showerror("Hata", f"Tarif detayları alınamadı: {e}")
        finally:
            cursor.close()
            db.close()

    def display_recipe_window(self, recipe):
        recipe_window = ctk.CTkToplevel(self.tarif_ara_pencere)
        recipe_window.title(recipe[0])
        center_window(recipe_window, 600, 500)
        recipe_window.resizable(False, False)
        recipe_window.attributes('-topmost', True)

        ctk.CTkLabel(
            recipe_window,
            text=recipe[0],
            font=("Arial", 16, "bold"),
            fg_color="transparent"
        ).pack(pady=10)

        ctk.CTkLabel(
            recipe_window,
            text="Malzemeler:",
            font=("Arial", 12, "bold"),
            fg_color="transparent"
        ).pack(anchor="w", padx=20)

        ingredients_text = ctk.CTkTextbox(recipe_window, width=500, height=100, font=("Arial", 12))
        ingredients_text.insert("1.0", recipe[1])
        ingredients_text.configure(state="disabled")
        ingredients_text.pack(pady=5)

        ctk.CTkLabel(
            recipe_window,
            text="Hazırlanışı:",
            font=("Arial", 12, "bold"),
            fg_color="transparent"
        ).pack(anchor="w", padx=20)

        content_text = ctk.CTkTextbox(recipe_window, width=500, height=200, font=("Arial", 12))
        content_text.insert("1.0", recipe[2])
        content_text.configure(state="disabled")
        content_text.pack(pady=5)

    def tarif_degerlendir_ekrani(self):
        self.degerlendir_pencere = ctk.CTkToplevel(self.pencere)
        self.degerlendir_pencere.title("Tarif Değerlendir")
        center_window(self.degerlendir_pencere, 400, 300)
        self.degerlendir_pencere.resizable(False, False)
        self.degerlendir_pencere.attributes('-topmost', True)

        ctk.CTkLabel(self.degerlendir_pencere, text="Değerlendirilecek Tarif Adı:", font=("Arial", 12, "bold"), fg_color="transparent").pack(pady=10)
        self.degerlendir_entry = ctk.CTkEntry(self.degerlendir_pencere, width=200)
        self.degerlendir_entry.pack(pady=5)

        ctk.CTkLabel(self.degerlendir_pencere, text="Puan (1-5):", font=("Arial", 12, "bold"), fg_color="transparent").pack(pady=10)
        self.puan_var = tk.IntVar(value=5)
        self.puan_scale = ctk.CTkSlider(self.degerlendir_pencere, from_=1, to=5, number_of_steps=4, variable=self.puan_var, width=200)
        self.puan_scale.pack(pady=5)

        ctk.CTkButton(
            self.degerlendir_pencere,
            text="Değerlendir",
            command=self.degerlendir,
            image=load_icon("rate"),
            compound="left",
            width=200,
            font=("Arial", 12, "bold"),
            fg_color="transparent",
            hover_color="#2F4F4F"
        ).pack(pady=10)
        self.degerlendirme_sonuc_label = ctk.CTkLabel(self.degerlendir_pencere, text="", font=("Arial", 12), fg_color="transparent")
        self.degerlendirme_sonuc_label.pack(pady=10)

    def degerlendir(self):
        tarif_adi = self.degerlendir_entry.get()
        puan = self.puan_var.get()

        if not tarif_adi:
            messagebox.showerror("Hata", "Lütfen değerlendirilecek tarif adını girin.")
            return

        db = connect_db()
        if db is None:
            return
        cursor = db.cursor()
        try:
            cursor.execute("SELECT id FROM recipes WHERE title = %s", (tarif_adi,))
            recipe = cursor.fetchone()
            if not recipe:
                messagebox.showerror("Hata", "Tarif bulunamadı.")
                return
            cursor.execute("INSERT INTO ratings (recipe_id, rating) VALUES (%s, %s)", (recipe[0], puan))
            db.commit()
            self.degerlendirme_sonuc_label.configure(text=f"{tarif_adi} için verilen puan: {puan}")
            messagebox.showinfo("Teşekkürler", "Tarif değerlendirmeniz için teşekkürler!")
            self.degerlendir_pencere.destroy()
        except mysql.Error as e:
            messagebox.showerror("Hata", f"Değerlendirme kaydedilemedi: {e}")
        finally:
            cursor.close()
            db.close()

    def malzeme_listesi_ekrani(self):
        self.malzeme_pencere = ctk.CTkToplevel(self.pencere)
        self.malzeme_pencere.title("Malzeme Listesi")
        center_window(self.malzeme_pencere, 400, 300)
        self.malzeme_pencere.resizable(False, False)
        self.malzeme_pencere.attributes('-topmost', True)

        ctk.CTkLabel(self.malzeme_pencere, text="Malzemesini görmek istediğiniz tarif adını girin:", font=("Arial", 12, "bold"), fg_color="transparent").pack(pady=10)
        self.malzeme_entry = ctk.CTkEntry(self.malzeme_pencere, width=200)
        self.malzeme_entry.pack(pady=5)

        ctk.CTkButton(
            self.malzeme_pencere,
            text="Malzeme Listesini Göster",
            command=self.malzeme_listesi_goster,
            image=load_icon("ingredient"),
            compound="left",
            width=200,
            font=("Arial", 12, "bold"),
            fg_color="transparent",
            hover_color="#2F4F4F"
        ).pack(pady=10)
        self.malzeme_sonuc_label = ctk.CTkLabel(self.malzeme_pencere, text="", font=("Arial", 12), fg_color="transparent")
        self.malzeme_sonuc_label.pack(pady=10)

    def malzeme_listesi_goster(self):
        tarif_adi = self.malzeme_entry.get()
        db = connect_db()
        if db is None:
            return
        cursor = db.cursor()
        try:
            cursor.execute("SELECT title, ingredients FROM recipes WHERE title = %s", (tarif_adi,))
            tarif = cursor.fetchone()
            if tarif:
                self.malzeme_sonuc_label.configure(text=f"{tarif[0]} için Malzemeler:\n{tarif[1]}")
            else:
                self.malzeme_sonuc_label.configure(text="Tarif bulunamadı.")
        except mysql.Error as e:
            messagebox.showerror("Hata", f"Veri okuma hatası: {e}")
        finally:
            cursor.close()
            db.close()

    def kullanici_profili_ekrani(self):
        self.profil_pencere = ctk.CTkToplevel(self.pencere)
        self.profil_pencere.title("Kullanıcı Profili")
        center_window(self.profil_pencere, 400, 300)
        self.profil_pencere.resizable(False, False)
        self.profil_pencere.attributes('-topmost', True)

        db = connect_db()
        cursor = db.cursor()
        cursor.execute("SELECT username FROM users WHERE id = %s", (self.user_id,))
        username = cursor.fetchone()[0]
        ctk.CTkLabel(self.profil_pencere, text=f"Kullanıcı Adı: {username}", font=("Arial", 12, "bold"), fg_color="transparent").pack(pady=10)

        ctk.CTkLabel(self.profil_pencere, text="Kaydettiğiniz Tarifler:", font=("Arial", 12, "bold"), fg_color="transparent").pack(pady=10)
        cursor.execute("SELECT title FROM recipes WHERE user_id = %s", (self.user_id,))
        tarifler = cursor.fetchall()
        cursor.close()
        db.close()

        if tarifler:
            tarif_listesi = "\n".join([t[0] for t in tarifler])
        else:
            tarif_listesi = "Henüz tarif kaydetmediniz."
        ctk.CTkLabel(self.profil_pencere, text=tarif_listesi, font=("Arial", 12), fg_color="transparent").pack(pady=5)

    def help_page(self):
        messagebox.showinfo("Nasıl Çalışır", "Bu uygulama ile tarif ekleyebilir, arayabilir, değerlendirebilir ve malzeme listelerini görebilirsiniz.")

    def about_page(self):
        messagebox.showinfo("Hakkında", "Zehra's Yemek Tarifi Uygulaması\nSürüm 1.0")

if __name__ == "__main__":
    LoginScreen()