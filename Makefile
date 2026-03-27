up:
	@docker build -t cv .
	@docker run  --rm -p 5000:5000 --name cv -v ./src:/app/src cv
down:
	@docker stop cv


