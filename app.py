from sentence_transformers import SentenceTransformer
from sklearn.preprocessing import normalize
from sklearn.metrics.pairwise import cosine_similarity

# Init is ran on server startup
# Load your model to GPU as a global variable here using the variable name "model"
def init():
    global model
    model = SentenceTransformer("sentence-transformers/paraphrase-mpnet-base-v2")


# Inference is ran for every server call
# Reference your preloaded global model variable here.
def inference(model_inputs: dict) -> dict:
    global model

    # Parse out your arguments
    prompt = model_inputs.get("prompt", None)
    if prompt == None:
        return {"message": "No prompt provided"}

    # Run the model
    sentence_embeddings = model.encode(prompt)
    normalized_embeddings = normalize(sentence_embeddings)

    # Detemine the similarity of the first sentence
    similarity =cosine_similarity(
        [sentence_embeddings[0]],
        sentence_embeddings[1:]
    )

    # Convert the output array to a list
    output = similarity.tolist()

    # Return the results as a dictionary
    return { "data": output }
