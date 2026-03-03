from playwright.sync_api import Page, expect

def test_borrar_canal_bot(page: Page):

    page.get_by_role("textbox", name='Buscar Bot...' ).fill('laura')
    

    page.locator("div.card-bot").filter(has_text="laura").click()
    
    page.get_by_role("paragraph").filter(has_text="Gestionar campañas").click()

    page.locator(".icon-trash.c-association__campaign-header-icon").click()
    
    page.get_by_role("button", name= "Eliminar").click()
    

    page.get_by_role("button", name= "Salir").click()

    expect(page.get_by_text('Se ha desasociado')).to_be_visible()