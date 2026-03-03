import os
import pytest
from playwright.sync_api import Page, expect

def test_exportar_bot_chattigo(page: Page):
    bot_card = page.locator("div.card-bot").filter(has_text="laura")

    bot_card.get_by_role("button").click()

    with page.expect_download() as download_info:
        page.get_by_role("paragraph").filter(has_text="Exportar proyecto").click()
    
    download = download_info.value
    
    path = f"./downloads/{download.suggested_filename}"
    download.save_as(path)
    
    assert os.path.exists(path), "El archivo no se descargó correctamente"
    
    expect(page.get_by_text("El proyecto se ha exportado")).to_be_visible()