"""Pagamentos

Revision ID: 75b5ffe8b348
Revises: d272b3ce18b6
Create Date: 2020-06-03 10:04:54.749663

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '75b5ffe8b348'
down_revision = 'd272b3ce18b6'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('forma_pagamento',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('descricao', sa.String(length=50), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pagamento',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('valor', sa.Float(), nullable=False),
        sa.Column('data_pagamento', sa.DateTime(), nullable=False),
        sa.Column('id_forma_pagamento', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['id_forma_pagamento'], ['forma_pagamento.id'], ),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table('pagamento_consulta',
        sa.Column('id_pagamento', sa.Integer(), nullable=False),
        sa.Column('id_consulta', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['id_consulta'], ['consulta.id'], ),
        sa.ForeignKeyConstraint(['id_pagamento'], ['pagamento.id'], ),
        sa.PrimaryKeyConstraint('id_pagamento', 'id_consulta')
    )

    op.alter_column('consulta', 'data',
               existing_type=sa.DATE(),
               type_=sa.DateTime(),
               existing_nullable=False)

def downgrade():
    op.alter_column('consulta', 'data',
               existing_type=sa.DateTime(),
               type_=sa.DATE(),
               existing_nullable=False)
    op.drop_table('pagamento_consulta')
    op.drop_table('pagamento')
    op.drop_table('forma_pagamento')
