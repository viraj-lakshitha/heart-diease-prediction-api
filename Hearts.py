from pydantic import BaseModel

# Model design to deploy in app.py
class Heart(BaseModel):
	age: int
	sex: int
	cp: int
	trestbps: int
	chol: int
	fbs: int
	restecg: int
	thalach: int
	exang: int
	oldpeak: float
	slope: int
	ca: int
	thal: int