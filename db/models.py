from sqlalchemy import Column, Integer, String, ForeignKey, BigInteger
from sqlalchemy.orm import relationship

from db.db import Base

class WordList(Base):
    __tablename__ = "wordlist"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    words = relationship("Word", back_populates="wordlist", lazy="selectin")


class Word(Base):
    __tablename__ = "word"

    id = Column(Integer, primary_key=True, index=True)
    original = Column(String, nullable=False)
    translation = Column(String, nullable=False)
    wordlist_id = Column(Integer, ForeignKey("wordlist.id"), nullable=False)

    wordlist = relationship("WordList", back_populates="words")


class UserWordList(Base):
    __tablename__ = "userwordlist"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(BigInteger, nullable=False)
    wordlist_id = Column(Integer, ForeignKey("wordlist.id"), nullable=False)


class UserWord(Base):
    __tablename__ = "userword"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(BigInteger, nullable=False)
    word_id = Column(Integer, ForeignKey("word.id"), nullable=False)
    learned = Column(Integer, nullable=False)
