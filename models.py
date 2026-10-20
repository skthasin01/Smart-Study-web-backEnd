
from database import Base
from sqlalchemy import Column,Integer,Float,Boolean,String,ForeignKey,Date,DateTime,Text
from datetime import datetime


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, nullable=False, index=True)
    hash_password = Column(String(255), nullable=False)
    role = Column(String(20), default="student", nullable=False)
    createAt = Column(DateTime, default=datetime.now, nullable=False)


class StudyTask(Base):
    __tablename__ = "studyTask"

    id = Column(Integer, primary_key=True, index=True)
    userId = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    difficulty = Column(String(20), nullable=False)
    estimateMinutes = Column(Integer, nullable=False)
    deadline = Column(DateTime, nullable=False)
    priority = Column(String(20), default="medium", nullable=False)
    status = Column(String(20), default="pending", nullable=False)


class StudyPlan(Base):
    __tablename__ = "studyPlan"

    id = Column(Integer, primary_key=True, index=True)
    userId = Column(Integer, ForeignKey("users.id"), nullable=False)
    planDate = Column(Date, nullable=False)
    availableMinutes = Column(Integer, nullable=False)
    totalPlanMinutes = Column(Integer, default=0, nullable=False)
    createAt = Column(DateTime, default=datetime.now, nullable=False)


class StudySession(Base):
    __tablename__ = "studySession"

    id = Column(Integer, primary_key=True, index=True)
    userId = Column(Integer, ForeignKey("users.id"), nullable=False)
    taskId = Column(Integer, ForeignKey("studyTask.id"), nullable=False)
    startTime = Column(DateTime, nullable=False)
    endTime = Column(DateTime, nullable=True)
    durationMinutes = Column(Integer, default=0, nullable=False)
    breakMinutes = Column(Integer, default=0, nullable=False)


class DailyCheckin(Base):
    __tablename__ = "dailyCheckin"

    id = Column(Integer, primary_key=True, index=True)
    userId = Column(Integer, ForeignKey("users.id"), nullable=False)
    checkInDate = Column(Date, nullable=False)
    stressLevel = Column(Integer, nullable=True)
    energyLevel = Column(Integer, nullable=True)
    moodLevel = Column(Integer, nullable=True)
    sleepHours = Column(Float, nullable=True)


class WorkloadAnalysis(Base):
    __tablename__ = "workloadAnalysis"

    id = Column(Integer, primary_key=True, index=True)
    userId = Column(Integer, ForeignKey("users.id"), nullable=False)
    analysisDate = Column(Date, nullable=False)
    workloadScore = Column(Float, nullable=False)
    totalTasks = Column(Integer, default=0, nullable=False)
    totalStudyMinutes = Column(Integer, default=0, nullable=False)
    riskLevel = Column(String(20), nullable=False)


class BurnoutAssessment(Base):
    __tablename__ = "burnoutAssessment"

    id = Column(Integer, primary_key=True, index=True)
    userId = Column(Integer, ForeignKey("users.id"), nullable=False)
    assessmentDate = Column(Date, nullable=False)
    riskScore = Column(Float, nullable=False)
    riskLevel = Column(String(20), nullable=False)
    reason = Column(Text, nullable=True)
    recommendation = Column(Text, nullable=True)


class Notification(Base):
    __tablename__ = "notification"

    id = Column(Integer, primary_key=True, index=True)
    userId = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String(200), nullable=False)
    message = Column(Text, nullable=False)
    type = Column(String(30), nullable=False)
    isRead = Column(Boolean, default=False, nullable=False)
    createAt = Column(DateTime, default=datetime.now, nullable=False)
