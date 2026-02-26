from playwright.sync_api import Page, expect

def test_filtrar_canales_exitoso(page: Page):
    page.locator(".b-filters__icon > .ch-icon").first.click()
    page.get_by_role("button", name="Seleccionar...").first.click()
    page.get_by_role("button", name="PruebasQA Parent").click()
    
    page.get_by_text("WEBCHAT").nth(2).click()
    page.get_by_text("WHATSAPP").click()
    
    page.get_by_role("button", name="Aplicar filtros").click()
    alerta_exito = page.get_by_text("Filtros aplicados con éxito")
    expect(alerta_exito).to_be_visible()

    page.get_by_role("button").nth(1).click()
    page.get_by_role("paragraph").filter(has_text="Gestionar campañas").click()
    
    expect(page.get_by_role("img", name="whatsapp-channel.svg")).to_be_visible()
    
    expect(page.get_by_role("img", name="widget-channel.svg")).to_be_visible()
    
    page.locator(".ch-ui-modal__close").first.click()