from enum import Enum

from pydantic import BaseModel, conint

from app.src.schemas.board import Board


class GameResultInput(BaseModel):
    board: Board
    start_position: dict       # Must be 0 or 23


class GameWinType(str, Enum):
    Oin = "oin"
    Mars = 'mars'
    Koks = 'koks'


class GameResultOutput(BaseModel):
    points: conint(ge=0)       # Number of points for a win
    win_type: GameWinType
