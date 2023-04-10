from typing import List, Optional, TypedDict

from pydantic import BaseModel


class Tree(BaseModel):
    value: int
    left: Optional["Tree"] = None
    right: Optional["Tree"] = None


class TreeDataNode(BaseModel):
    id: str
    left: Optional[str] = None
    right: Optional[str] = None
    value: int


class Nodes(BaseModel):
    nodes: List[TreeDataNode]
    root: str


class TreeData(BaseModel):
    tree: Nodes
