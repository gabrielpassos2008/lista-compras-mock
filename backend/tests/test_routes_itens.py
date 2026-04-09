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
        
@patch("app.routes.items.item_service")
class TestRotasPostCadastroItem:
    def test_post_cadastrar_item(self, mock_svc, client):
        mock_svc.create_item.return_value = ShoppingItem(id=1, name="feijão", quantity=2, purchased= True)
        resp = client.post("api/items")
        assert resp.status_code == 201
        assert resp.get_json() == {
            "id": 1, "name": "feijão", "quantity":2, "purchased": True
        }
        mock_svc.create_item.assert_called_once()
        
@patch("app.routes.items.item_service")       
class TestRotasDeleteItemPorId:
    def test_delete_item_por_id(self, mock_svc,client):
        mock_svc.delete_item.return_value = ShoppingItem(id=2, name="carne", quantity=1, purchased= True)
        resp = client.delete("api/items/2")
        assert resp.status_code == 204

        mock_svc.delete_item.assert_called_once()