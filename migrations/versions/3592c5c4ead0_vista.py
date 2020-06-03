"""Vista

Revision ID: 3592c5c4ead0
Revises: 20977383b6c5
Create Date: 2020-06-03 14:12:25.340415

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3592c5c4ead0'
down_revision = '20977383b6c5'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('forma_pagamento', sa.Column('vista', sa.Boolean(), nullable=False))


def downgrade():
    op.drop_column('forma_pagamento', 'vista')
