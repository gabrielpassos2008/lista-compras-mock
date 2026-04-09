from unittest.mock import patch
from app.models.item import ShoppingItem


@patch("app.routes.items.item_service")
class TestRotasListagemItensPorId:  
    def test_get_listagem_itens_por_id_mock(self,mock_svc, client):
        mock_svc.get_item.return_value = ShoppingItem(id=1, name="arroz", quantity=3,purchased=False)
        
        resp = client.get("/api/items/1")
        assert resp.status_code == 200  
        assert resp.get_json() == {
             "id": 1, "name": "arroz", "quantity":3, "purchased": False
        }
        mock_svc.get_item.assert_called_once()
        

    
