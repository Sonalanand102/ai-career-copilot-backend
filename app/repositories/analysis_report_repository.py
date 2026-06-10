from uuid import UUID

from sqlalchemy import select

from app.models.analysis_report import (
    AnalysisReport
)


class AnalysisReportRepository:

    def __init__(self, db):
        self.db = db

    def create(self, report):

        self.db.add(report)

        self.db.commit()

        self.db.refresh(report)

        return report

    def get_by_analysis_id(self, analysis_id: UUID):
        stmt = select(AnalysisReport).where(AnalysisReport.analysis_id == analysis_id)
        return list(self.db.scalars(stmt))