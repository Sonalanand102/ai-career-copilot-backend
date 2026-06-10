from uuid import UUID

from sqlalchemy import select

from app.models.analysis import Analysis


class AnalysisRepository:

    def __init__(self, db):
        self.db = db

    def create(
        self,
        analysis: Analysis
    ):

        self.db.add(
            analysis
        )

        self.db.commit()

        self.db.refresh(
            analysis
        )

        return analysis

    def get_by_id(self, analysis_id: UUID):
        stmt = select(Analysis).where(Analysis.id == analysis_id)
        return self.db.scalar(stmt)