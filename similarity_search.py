from datetime import datetime
from database.vector_store import VectorStore
from services.synthesizer import Synthesizer
from timescale_vector import client

# Initialize VectorStore
vec = VectorStore()

# --------------------------------------------------------------
# Shipping question
# --------------------------------------------------------------

relevant_question = "gold dealers"
results = vec.search(relevant_question)
print("results ::", results)
# print(results["email"].head())
# response = Synthesizer.generate_response(question=relevant_question, context=results)
# #
# print(f"\n{response.answer}")
# print("\nThought process:")
# for thought in response.thought_process:
#     print(f"- {thought}")
# print(f"\nContext: {response.enough_context}")
# #
# # # --------------------------------------------------------------
# # # Irrelevant question
# # # --------------------------------------------------------------
# #
# irrelevant_question = "How's the weather today?"
#
# results = vec.search(irrelevant_question, limit=3)
# print("results ::", results)
# # response = Synthesizer.generate_response(question=irrelevant_question, context=results)
# # #
# print(f"\n{response.answer}")
# print("\nThought process:")
# for thought in response.thought_process:
#     print(f"- {thought}")
# print(f"\nContext: {response.enough_context}")
#
# # --------------------------------------------------------------
# # Metadata filtering
# # --------------------------------------------------------------
#
# metadata_filter = {"industry": "Gold"}
# # relevant_question = "Who is at risk for Parasites – Schistosomiasis?"
# results = vec.search(relevant_question, limit=3, metadata_filter=metadata_filter)
# print("results ::", results)
# #
# response = Synthesizer.generate_response(question=relevant_question, context=results)
#
# print(f"\n{response.answer}")
# print("\nThought process:")
# for thought in response.thought_process:
#     print(f"- {thought}")
# print(f"\nContext: {response.enough_context}")
#
# # --------------------------------------------------------------
# # Advanced filtering using Predicates
# # --------------------------------------------------------------
#
# predicates = client.Predicates("question_type", "==", "information")
# print("predicates ::", predicates)
# results = vec.search(relevant_question, limit=3, predicates=predicates)
# print("results ::", results)
#
# predicates = client.Predicates("question_type", "==", "prevention") | client.Predicates(
#     "category", "==", "Services"
# )
# results = vec.search(relevant_question, limit=3, predicates=predicates)
#
# predicates = client.Predicates("question_type", "==", "frequency") & client.Predicates(
#     "created_at", ">", "2024-10-08"
# )
# results = vec.search(relevant_question, limit=3, predicates=predicates)
# #
# # --------------------------------------------------------------
# # Time-based filtering
# # --------------------------------------------------------------
#
# # September — Returning results
# time_range = (datetime(2024, 9, 1), datetime(2024, 9, 30))
# results = vec.search(relevant_question, limit=3, time_range=time_range)
#
# # August — Not returning any results
# time_range = (datetime(2024, 8, 1), datetime(2024, 8, 30))
# results = vec.search(relevant_question, limit=3, time_range=time_range)
