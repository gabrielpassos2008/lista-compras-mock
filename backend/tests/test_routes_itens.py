from unittest.mock import patch
from app.models.item import ShoppingItem 
from app.services.item_service import ItemValidationError


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
        
    def test_get_listagem_itens_nao_existente_por_id_mock(self, mock_svc,client):
        mock_svc.get_item.return_value = None
        resp = client.get("/api/items/1")
        assert resp.status_code == 404
        mock_svc.get_item.assert_called_once()
        
@patch("app.routes.items.item_service")
class TestRotasPostCadastroItem:
    def test_post_cadastrar_item_mock(self, mock_svc, client):
        mock_svc.create_item.return_value = ShoppingItem(id=1, name="feijão", quantity=2, purchased= True)
        resp = client.post("api/items")
        assert resp.status_code == 201
        assert resp.get_json() == {
            "id": 1, "name": "feijão", "quantity":2, "purchased": True
        }
        mock_svc.create_item.assert_called_once()
    
    def test_post_cadastrar_item_erro_mock(self,mock_svc,client):
        mock_svc.create_item.side_effect = ItemValidationError("O nome do item é obrigatório.", code="name_required")
        resp = client.post("api/items")
        assert resp.status_code == 400
        mock_svc.create_item.assert_called_once()
        
@patch("app.routes.items.item_service")       
class TestRotasDeleteItemPorId:
    def test_delete_item_por_id_mock(self, mock_svc,client):
        mock_svc.delete_item.return_value = ShoppingItem(id=2, name="carne", quantity=1, purchased= True)
        resp = client.delete("api/items/2")
        assert resp.status_code == 204
        mock_svc.delete_item.assert_called_once()
        
    def test_delete_item_nao_existente_por_id_mock(self,mock_svc,client):
        mock_svc.delete_item.return_value = None
        resp = client.delete("api/items/90")
        assert resp.status_code == 404
        mock_svc.delete_item.assert_called_once()
        
@patch("app.routes.items.item_service")
class TestRotasPutPorId:
    def test_put_item_por_id_mock(self, mock_svc, client):
        mock_svc.update_item.return_value = ShoppingItem(id=1, name="arroz", quantity=10, purchased=True)
        resp = client.put("api/items/1")
        assert resp.status_code == 200
        assert resp.get_json() == {
            "id":1, "name":"arroz", "quantity":10, "purchased":True
        }
        mock_svc.update_item.assert_called_once()