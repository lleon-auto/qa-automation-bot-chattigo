from playwright.sync_api import Page, expect

def test_eliminar_bot_chattigo(page: Page):
    page.get_by_role("textbox", name="Buscar Bot...").fill("laura")
    
    page.locator("div.card-bot").filter(has_text="laura").get_by_role("button").click()

    page.get_by_role("paragraph").filter(has_text="Eliminar proyecto").click()

    page.get_by_role("button", name="Aceptar").click()

    success_message = page.get_by_text("Se ha eliminado el bot")
    expect(success_message).to_be_visible()