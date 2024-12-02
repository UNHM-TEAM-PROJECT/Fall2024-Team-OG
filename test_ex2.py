import csv
import os
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from deepeval.metrics import AnswerRelevancyMetric, GEval, FaithfulnessMetric
import pytest
import deepeval
from deepeval import assert_test
from deepeval.dataset import EvaluationDataset
from deepeval.test_case import LLMTestCase, LLMTestCaseParams
from deepeval.metrics import AnswerRelevancyMetric, GEval, ContextRelevancyMetric, FaithfulnessMetric

API_KEY = "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"
os.environ["OPENAI_API_KEY"] = API_KEY

dataset = EvaluationDataset()

test_cases = [
    LLMTestCase(
        input="What is COMP690 again?",
        actual_output="COMP690 is the Internship Experience course for undergraduate students.",
        expected_output="COMP690 is the Internship Experience course for undergraduate students. It's a 4-credit course that can be taken when you have an internship or are working in a tech job.",
        retrieval_context=["COMP690 is required for all computing majors"]
    ),
    LLMTestCase(
        input="Generate a castle school in fantasy land with the words LLM evaluation on it",
        actual_output="[MLLMImage(url='./data/image.webp', local=True)]",
        expected_output="A fantasy castle school image with 'LLM evaluation' text",
        retrieval_context=None
    )
]

for test_case in test_cases:
    dataset.add_test_case(test_case)

answer_relevancy_metric = AnswerRelevancyMetric(threshold=0.5)
correctness_metric = GEval(
    name="Correctness",
    criteria="Correctness - determine if the actual output is correct according to the expected output.",
    evaluation_params=[
        LLMTestCaseParams.ACTUAL_OUTPUT,
        LLMTestCaseParams.EXPECTED_OUTPUT,
    ]
)
context_relevancy_metric = ContextRelevancyMetric()
faithfulness_metric = FaithfulnessMetric(threshold=0.7)

@pytest.mark.parametrize("test_case", dataset)
def test_chatbot(test_case: LLMTestCase):
    assert_test(test_case, [
        answer_relevancy_metric,
        correctness_metric,
        context_relevancy_metric,
        faithfulness_metric
    ])

prompt_template = ChatPromptTemplate.from_messages([
    ("system", """
    You are a friendly internship advisor for UNH Manchester's computing program. 
    Your responses should be direct, helpful, and natural - like talking to a student in person.
    """),
    MessagesPlaceholder(variable_name="messages"),
])

@deepeval.log_hyperparameters(model="gpt-3.5-turbo", prompt_template=prompt_template.messages[0].prompt.template)
def hyperparameters():
    return {"temperature": 0.7, "max_tokens": 150, "top_p": 1}

if __name__ == "__main__":
    pytest.main([__file__])

