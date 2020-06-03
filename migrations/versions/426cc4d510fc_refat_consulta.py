"""Refat Consulta

Revision ID: 426cc4d510fc
Revises: 3592c5c4ead0
Create Date: 2020-06-03 14:22:29.550707

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '426cc4d510fc'
down_revision = '3592c5c4ead0'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_table('pagamento_consulta')
    op.add_column('pagamento', sa.Column('id_consulta', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'pagamento', 'consulta', ['id_consulta'], ['id'])


def downgrade():
    op.drop_constraint(None, 'pagamento', type_='foreignkey')
    op.drop_column('pagamento', 'id_consulta')
    op.create_table('pagamento_consulta',
        sa.Column('id_pagamento', sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column('id_consulta', sa.INTEGER(), autoincrement=False, nullable=False),
        sa.ForeignKeyConstraint(['id_consulta'], ['consulta.id'], name='pagamento_consulta_id_consulta_fkey'),
        sa.ForeignKeyConstraint(['id_pagamento'], ['pagamento.id'], name='pagamento_consulta_id_pagamento_fkey'),
        sa.PrimaryKeyConstraint('id_pagamento', 'id_consulta', name='pagamento_consulta_pkey')
    )
