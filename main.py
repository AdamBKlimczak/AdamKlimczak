import flet as ft
import os

def main(page: ft.Page):
    page.title = "Adam Klimczak - Compensation & Benefits Expert"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.scroll = "auto"
    page.bgcolor = "#F8F9FA"
    page.padding = 0

    # --- PALETA BARW (Profesjonalna analityka) ---
    primary = "#1A237E"  # Navy Blue
    secondary = "#0D47A1"
    accent = "#00C853"   # Green (akcent danych/zysku)
    bg_white = ft.colors.WHITE

    # --- KOMPONENTY ---
    def skill_chip(label):
        return ft.Chip(
            label=ft.Text(label, size=12, weight=ft.FontWeight.W_500),
            bgcolor="#E8EAF6",
            border_radius=5
        )

    def exp_entry(title, company, date, location, description=""):
        return ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Text(title, size=18, weight=ft.FontWeight.BOLD, color=primary),
                    ft.Text(date, size=13, italic=True, color="grey"),
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                ft.Text(f"{company} | {location}", size=14, weight=ft.FontWeight.W_500),
                ft.Text(description, size=14, color="#455A64") if description else ft.Container(),
                ft.Divider(height=20, thickness=0.5),
            ], spacing=5),
            padding=ft.padding.only(bottom=10)
        )

    # --- TREŚĆ ---
    content_area = ft.Container(
        width=900,
        bgcolor=bg_white,
        padding=50,
        border_radius=15,
        shadow=ft.BoxShadow(blur_radius=25, color=ft.colors.with_opacity(0.05, "black")),
        content=ft.Column([
            # NAGŁÓWEK
            ft.Row([
                ft.Column([
                    ft.Text("ADAM KLIMCZAK", size=40, weight=ft.FontWeight.BOLD, color=primary, letter_spacing=1),
                    ft.Text("Ekspert ds. analiz wynagrodzeń | Analityk Biznesowy", size=20, color=secondary),
                    ft.Row([
                        ft.Icon(ft.icons.EMAIL, size=18, color=secondary),
                        ft.Text("klimczak@sedlak.pl", size=14),
                        ft.Container(width=15),
                        ft.Icon(ft.icons.PHONE, size=18, color=secondary),
                        ft.Text("503 331 902", size=14),
                    ]),
                ], expand=True),
                ft.Container(
                    content=ft.Icon(ft.icons.ANALYTICS, size=80, color=primary),
                    padding=20
                )
            ]),

            ft.Divider(height=40, thickness=2, color=primary),

            # O MNIE
            ft.Text("O MNIE", size=20, weight=ft.FontWeight.BOLD, color=primary),
            ft.Text(
                "Dogaduję się z danymi. Przy pomocy Excela, Pythona (Pandas) i Tableau potrafię wycisnąć z bazy danych wszystko. "
                "Tworzę najlepsze raporty płacowe w Polsce, łącząc pasję do automatyzacji (VBA) z precyzyjną analizą rynku pracy.",
                size=15, line_height=1.4
            ),

            ft.Container(height=20),

            # UMIEJĘTNOŚCI TECHNICZNE
            ft.Text("STACK TECHNICZNY", size=18, weight=ft.FontWeight.BOLD, color=primary),
            ft.Row([
                skill_chip("Python (Pandas)"),
                skill_chip("Advanced Excel / VBA"),
                skill_chip("Tableau"),
                skill_chip("Analiza Danych"),
                skill_chip("Wizualizacja"),
            ], wrap=True),

            ft.Container(height=20),

            # DOŚWIADCZENIE
            ft.Text("DOŚWIADCZENIE ZAWODOWE", size=20, weight=ft.FontWeight.BOLD, color=primary),
            exp_entry("Ekspert ds. analiz wynagrodzeń", "Sedlak & Sedlak", "sty 2025 – Obecnie", "Kraków (Hybrydowo)", 
                      "Wartościowanie stanowisk, analizy luki płacowej, audyty systemów wynagradzania."),
            exp_entry("Starszy specjalista ds. analiz wynagrodzeń", "Sedlak & Sedlak", "2022 – 2024", "Kraków"),
            exp_entry("Specjalista ds. analiz wynagrodzeń", "Sedlak & Sedlak", "2019 – 2022", "Kraków"),
            exp_entry("Nauczyciel Podstaw przedsiębiorczości", "ZSM 4", "2020 – 2021", "Kraków"),
            exp_entry("Referent ds. księgowych", "MCOO", "2017 – 2018", "Kraków"),

            # WYKSZTAŁCENIE
            ft.Text("EDUKACJA", size=20, weight=ft.FontWeight.BOLD, color=primary),
            ft.ListTile(
                leading=ft.Icon(ft.icons.SCHOOL, color=secondary),
                title=ft.Text("Analityk Biznesowy (Studia Podyplomowe)"),
                subtitle=ft.Text("Krakowska Szkoła Biznesu UEK"),
            ),
            ft.ListTile(
                leading=ft.Icon(ft.icons.SCHOOL, color=secondary),
                title=ft.Text("Magister Ekonomii (Analityka Ekonomiczno-Finansowa)"),
                subtitle=ft.Text("Uniwersytet Ekonomiczny w Krakowie"),
            ),

            # PRZYCISKI KONTAKTOWE
            ft.Container(height=30),
            ft.Row([
                ft.ElevatedButton(
                    "Pobierz ofertę (Analiza luki)", 
                    icon=ft.icons.INSERT_CHART,
                    on_click=lambda _: page.launch_url("mailto:klimczak@sedlak.pl"),
                    style=ft.ButtonStyle(bgcolor=primary, color="white")
                ),
                ft.TextButton("Zadzwoń: 503 331 902", on_click=lambda _: page.launch_url("tel:503331902"))
            ], alignment=ft.MainAxisAlignment.CENTER)
        ], spacing=10)
    )

    page.add(
        ft.Container(
            content=content_area,
            alignment=ft.alignment.center,
            padding=40
        )
    )

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8502))
    ft.app(target=main, view=ft.AppView.WEB_BROWSER, host="0.0.0.0", port=port)