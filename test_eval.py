import pytest
import deepeval
from deepeval import assert_test
from deepeval.dataset import EvaluationDataset
from deepeval.test_case import LLMTestCase, LLMTestCaseParams
from deepeval.metrics import AnswerRelevancyMetric, GEval, ContextRelevancyMetric, FaithfulnessMetric

# Load dataset from your CSV file
dataset = EvaluationDataset(alias="UNH Computing Chatbot Dataset")

dataset.add_test_cases_from_csv_file(
    file_path="Fall 24 - Chatbot Auto Test Cases.csv",
    input_column="input",
    expected_output_column="expected_output",
    retrieval_context_column="retrieval_context",
    id_column="Test Case ID"
)

# Define metrics
answer_relevancy_metric = AnswerRelevancyMetric(threshold=0.7)
correctness_metric = GEval(
    name="Correctness",
    criteria="Correctness - determine if the actual output is correct according to the expected output.",
    evaluation_params=[
        LLMTestCaseParams.ACTUAL_OUTPUT,
        LLMTestCaseParams.EXPECTED_OUTPUT,
    ],
    strict=True,
)
context_relevancy_metric = ContextRelevancyMetric(threshold=0.5)
faithfulness_metric = FaithfulnessMetric(threshold=0.7)


# Test function
@pytest.mark.parametrize("test_case", dataset)
def test_chatbot(test_case: LLMTestCase):
    # Here, you would typically call your chatbot to get the actual output
    # For this example, we'll use a placeholder function
    actual_output = get_chatbot_response(test_case.input)

    # Update the test case with the actual output
    test_case.actual_output = actual_output

    assert_test(test_case, [
        answer_relevancy_metric,
        correctness_metric,
        context_relevancy_metric,
        faithfulness_metric
    ])


# Placeholder function for getting chatbot response
def get_chatbot_response(input_text):
    # Replace this with your actual chatbot logic
    return "This is a placeholder response"


# Hyperparameters logging
@deepeval.log_hyperparameters(model="your-model-name", prompt_template="Your prompt template...")
def hyperparameters():
    return {"temperature": 0.7, "max_tokens": 150, "top_p": 1}


# Main execution
if __name__ == "__main__":
    pytest.main([__file__])