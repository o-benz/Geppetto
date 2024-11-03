FROM public.ecr.aws/lambda/python:3.10

# Copy requirements.txt and install dependencies
COPY requirements.txt ${LAMBDA_TASK_ROOT}
RUN pip install -r requirements.txt


# Copy lambda_function.py
COPY lambda_function.py ${LAMBDA_TASK_ROOT}


CMD ["lambda_function.lambda_handler"]