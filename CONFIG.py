# encoding: utf-8

# path of saving model
BASE_MODEL_DIR = 'model'

# name of model
MODEL_NAME = 'chatbot_model.ckpt'
# MODEL_NAME = 'chatbot_model_baseline.ckpt'
# number of epochs
n_epoch = 30
# batch size of sampling
batch_size = 256
# the percentage of saving nerual when doing dropout
keep_prob = 0.7

# settings of corpus
data_config = {
    # minimum size of question
    "min_q_len": 1,
    # maximum size of question
    "max_q_len": 20,
    # minimum size of answer
    "min_a_len": 2,
    # maximum size of answer
    "max_a_len": 20,
    # file of word and index
    "word2index_path": "data/w2i.pkl",
    # original word vector
    "word_vec_path": "data/word_vec.pkl",
    # generated embedding word vector
    "emb_path": "data/emb.pkl",
    # original corpus
    "path": "clean_chat_corpus/",
    # original corpus after preprocessing
    "processed_path": "data/data.pkl",
}

model_config = {
    "hidden_size": 256,
    "cell_type": "lstm",
    "layer_size": 4,
    "embedding_dim": 300,
    "share_embedding": True,
    "max_decode_step": 80,
    "max_gradient_norm": 3.0,
    "learning_rate": 0.001,
    "decay_step": 100000,
    "min_learning_rate":1e-6,
    "bidirection":True,
    "beam_width":200
}