import flet as ft
import os

def main(page: ft.Page):
    page.title = "Adam Klimczak - CV"
    page.theme_mode = ft.ThemeMode.LIGHT
    # ScrollMode.AUTO został w niektórych wersjach zastąpiony prostym True/False lub "auto"
    page.scroll = "auto" 
    page.bgcolor = "#F8F9FA"
    page.padding = 0

    # --- KOLORY (Wersja 0.27+) ---
    primary_color = "#1A237E"
    secondary_color = "#0D47A1"

    # --- KOMPONENTY ---
    def skill_chip(label):
        # Maksymalnie uproszczony Chip - bez border_radius, który sypał błędem
        return ft.Chip(
            label=ft.Text(label, size=12),
            bgcolor="#E8EAF6"
        )

    def exp_entry(title, company, date, location, description=""):
        return ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Text(title, size=18, weight="bold", color=primary_color),
                    ft.Text(date, size=13, italic=True, color="grey"),
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                ft.Text(f"{company} | {location}", size=14, weight="w500"),
                ft.Text(description, size=14, color="#455A64") if description else ft.Container(),
                ft.Divider(height=20, thickness=0.5),
            ], spacing=5),
            padding=ft.padding.only(bottom=10)
        )

    # --- STRUKTURA CV ---
    content_area = ft.Container(
        width=900,
        bgcolor=ft.Colors.WHITE,
        padding=50,
        border_radius=15,
        shadow=ft.BoxShadow(blur_radius=25, color=ft.Colors.with_opacity(0.1, ft.Colors.BLACK)),
        content=ft.Column([
            # NAGŁÓWEK
            ft.Row([
                ft.Column([
                    ft.Text("ADAM KLIMCZAK", size=40, weight="bold", color=primary_color),
                    ft.Text("Ekspert ds. analiz wynagrodzeń | Analityk Biznesowy", size=20, color=secondary_color),
                    ft.Row([
                        ft.Icon(ft.Icons.MAIL_OUTLINE, size=18, color=secondary_color),
                        ft.Text("klimczak@sedlak.pl", size=14),
                        ft.Container(width=15),
                        ft.Icon(ft.Icons.PHONE_ANDROID, size=18, color=secondary_color),
                        ft.Text("503 331 902", size=14),
                    ]),
                ], expand=True),
                ft.Container(
                    content=ft.Icon(ft.Icons.QUERY_STATS, size=80, color=primary_color),
                    padding=20
                )
            ]),

            ft.Divider(height=40, thickness=2, color=primary_color),

            # O MNIE
            ft.Text("O MNIE", size=22, weight="bold", color=primary_color),
            ft.Text(
                "Dogaduję się z danymi. Przy pomocy Excela, Pythona (Pandas) i Tableau potrafię wycisnąć z bazy danych wszystko. "
                "Tworzę najlepsze raporty płacowe w Polsce, łącząc pasję do automatyzacji (VBA) z precyzyjną analizą rynku pracy.",
                size=15
            ),

            ft.Container(height=15),

            # PROJEKTY
            ft.Container(
                content=ft.Column([
                    ft.Text("KOMPLEKSOWE PROJEKTY WARTOŚCIOWANIA", size=18, weight="bold", color=primary_color),
                    ft.Text(
                        "Prowadzę pełne procesy wartościowania stanowisk w organizacjach, obejmujące:",
                        size=14, weight="bold"
                    ),
                    ft.Text(
                        "• Analizę stanowisk i dobór odpowiedniej metody wartościowania.\n"
                        "• Przygotowanie dedykowanych narzędzi analitycznych.\n"
                        "• Wybór i szkolenie komisji wartościującej oraz moderowanie sesji.\n"
                        "• Opracowanie finalnej struktury i tabel płac zgodnych z rynkiem.",
                        size=14
                    ),
                ], spacing=5),
                bgcolor="#F1F3F9",
                padding=20,
                border_radius=10
            ),

            ft.Container(height=20),

            # SKILLS
            ft.Text("STACK TECHNICZNY", size=18, weight="bold", color=primary_color),
            ft.Row([
                skill_chip("Python (Pandas)"),
                skill_chip("Advanced Excel / VBA"),
                skill_chip("Tableau"),
                skill_chip("Analiza Danych"),
                skill_chip("Modelowanie tabel płac"),
            ], wrap=True),

            ft.Container(height=20),

            # EXP
            ft.Text("DOŚWIADCZENIE ZAWODOWE", size=22, weight="bold", color=primary_color),
            exp_entry("Ekspert ds. analiz wynagrodzeń", "Sedlak & Sedlak", "sty 2025 – Obecnie", "Kraków"),
            exp_entry("Starszy specjalista ds. analiz wynagrodzeń", "Sedlak & Sedlak", "2022 – 2024", "Kraków"),
            exp_entry("Specjalista ds. analiz wynagrodzeń", "Sedlak & Sedlak", "2019 – 2022", "Kraków"),
            exp_entry("Nauczyciel Podstaw przedsiębiorczości", "ZSM 4", "2020 – 2021", "Kraków"),

            # EDU
            ft.Text("EDUKACJA", size=22, weight="bold", color=primary_color),
            ft.ListTile(
                leading=ft.Icon(ft.Icons.SCHOOL, color=secondary_color),
                title=ft.Text("Analityk Biznesowy (Studia Podyplomowe)"),
                subtitle=ft.Text("Krakowska Szkoła Biznesu UEK"),
            ),
            ft.ListTile(
                leading=ft.Icon(ft.Icons.SCHOOL, color=secondary_color),
                title=ft.Text("Magister Ekonomii (Analityka Ekonomiczno-Finansowa)"),
                subtitle=ft.Text("Uniwersytet Ekonomiczny w Krakowie"),
            ),

            ft.Container(height=30),
            
            # CTA
            ft.Row([
                ft.ElevatedButton(
                    "Skontaktuj się w sprawie projektu", 
                    icon=ft.Icons.SEND,
                    on_click=lambda _: page.launch_url("mailto:klimczak@sedlak.pl"),
                    style=ft.ButtonStyle(bgcolor=primary_color, color=ft.Colors.WHITE)
                ),
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
    # Host 0.0.0.0 jest kluczowy dla Rendera
    ft.app(target=main, view=ft.AppView.WEB_BROWSER, host="0.0.0.0", port=port)