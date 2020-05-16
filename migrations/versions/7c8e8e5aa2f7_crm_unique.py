"""CRM unique

Revision ID: 7c8e8e5aa2f7
Revises: 54ac2f496f4b
Create Date: 2020-05-13 14:02:43.754195

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c8e8e5aa2f7'
down_revision = '54ac2f496f4b'
branch_labels = None
depends_on = None


def upgrade():
    op.create_unique_constraint(None, 'medico', ['crm'])


def downgrade():
    op.drop_constraint(None, 'medico', type_='unique')
