from playwright.sync_api import Page, expect

def test_ediar_canal_bot(page: Page):
    page.get_by_role("textbox", name="Buscar Bot...").fill("laura")
    page.get_by_role("button").nth(1).click()
    page.get_by_role("paragraph").filter(has_text="Gestionar campañas").click()
    page.locator(".icon-pencil-edit").click()
    page.get_by_title("pruebasqaparent3607-9707-").click()
    page.get_by_role("button", name="Guardar").click()
    page.get_by_role("button", name="Salir").click()

    expect(page.get_by_role("textbox", name="Buscar Bot...")).to_be_visible()