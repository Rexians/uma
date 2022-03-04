from fastapi import FastAPI, HTTPException, APIRouter
from ..models.mcoc_nodes import Nodes

router = APIRouter()

@router.get("/nodes")
def read_all_nodes():
    """
    Reads all the nodes
    """

    nodes_info = Nodes()
    try:
        nodes = nodes_info.read_all_nodes()
        nodes_dict = {
                "data" : nodes['data'],
                "status" : 200,
                "detail" : "Successful"
                }
        return nodes_dict
    except Exception as e:
        if isinstance(e, FileNotFoundError):
            raise HTTPException(status_code=404,detail='404: '+nodes_info.error)


@router.get("/nodes/{node_id}")
def read_node(node_id):

    node = Nodes()
    try:
        node.read_node(node_id)
        node_dict = {
                'node_id': node.node_id,
                'node_name': node.node_name,
                'node_info': node.node_info,
                'status' : 200,
                'detail' : 'Successful'
                }
        return node_dict
    except Exception as e:
        if isinstance(e, FileNotFoundError):
            raise HTTPException(status_code=404,detail='404: '+node.error)
        elif isinstance(e, KeyError):
            raise HTTPException(status_code=400, detail='400: '+node.error)
        else:
            raise e    