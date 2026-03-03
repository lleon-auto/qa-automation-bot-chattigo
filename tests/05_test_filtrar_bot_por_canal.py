from playwright.sync_api import Page, expect

def test_filtrar_por_canal(page: Page):
    page.locator(".b-filters__icon").click()
    page.get_by_role("button", name="Seleccionar...").first.click()
    page.get_by_role("button", name="PruebasQA Parent").click()
    
    page.locator('label').filter(has_text= 'WEBCHAT').nth(2).click()
    
    page.get_by_role("button", name="Aplicar filtros").click()
    expect(page.get_by_text("Filtros aplicados con éxito")).to_be_visible()