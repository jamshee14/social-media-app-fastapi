"""add content table

Revision ID: bf15409041b9
Revises: 42f4dcda1e3d
Create Date: 2026-02-27 00:45:25.420767

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bf15409041b9'
down_revision: Union[str, Sequence[str], None] = '42f4dcda1e3d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
