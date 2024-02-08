from unittest.mock import patch
from src.drivers.barcode_handler import BarcodeHandler
from src.controllers.tag_creator_controller import TagCreatorController


@patch.object(BarcodeHandler, 'create_barcode')
def test_create(mock_create_barcode):
    mock_value = 'image_path'
    mock_create_barcode.return_value = mock_value
    tag_creator_controller = TagCreatorController()

    result = tag_creator_controller.create(mock_value)

    assert isinstance(result, dict)
    assert result == {'data': {'type': 'Tag Image', 'count': 1, 'path': 'image_path.png'}}