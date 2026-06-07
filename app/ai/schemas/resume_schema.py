from typing import Any

from pydantic import BaseModel
from pydantic import Field


class ResumeSchema(BaseModel):

    skills: list[str] = Field(default_factory=list)

    projects: list[Any] = Field(default_factory=list)

    experience: list[Any] = Field(default_factory=list)

    education: list[Any] = Field(default_factory=list)

    certifications: list[Any] = Field(default_factory=list)

    achievements: list[Any] = Field(default_factory=list)