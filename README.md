# FinGPT - TransformerPrediction: jceltruda's branch

**My overarching goal for this project is to gain ML and LLM knowledge and skills that will serve me in future development.**

Here is a brief log of the information I have learned from this project:

**Transformer model:**

A transformer is a special kind of neural network and is the architecture used in all popular commercial LLMs. The defining feature of transformers is that they have a mechanism called attention that allows the models to assess the importance of different input elements.

**Learned about training and loss function:**

Our assignment for this project is to improve the model’s stock prediction abilities by improving its cross entropy loss function. This is a function that models the error of the model, the difference between the correct/best output and the actual output. This isn’t a function that we design ourselves, rather one that the model constructs itself through training.

Training is a process where a model is fed lots of data so that it can learn overtime and gradually improve its knowledge through optimization techniques and algorithms. The model continuously updated its parameters in an attempt to minimize the loss function. The process of re-training a pretrained model to make it better at a specific task is often referred to as “fine-tuning”. This is what we will do to improve stock prediction capabilities.

**Data Processing:**

Data is a crucial element of machine learning as it is through data that models learn correlations, patterns, and features of what they are being trained on. For Llama 2-7b, data for training must be in this format:

{"input": "What color is the sky?", "output": "The sky is blue."}

When training more

You can actually train the model easily, using predefined functions from a variety of libraries, including HuggingFace’s Transformers library.

**Llama 2 model:**

Llama 2 is Meta’s current flagship LLM, which is commonly considered open source as you can use the model freely after securing a license from Meta. The model comes in several different sizes, with the one we are using having 7 billion parameters. Because it has been open sourced, many organizations and individuals have created libraries to easily modify and train the model, making it ideal for our project.

**Development environment:**

We are using Google Colab for this project, which is an online platform where you can run python code and use TPUs and GPUs for free. This platform has helped to make machine learning and AI practice and development more accessible as the hardware needed to train models can be very expensive.

**Resources used to gather this knowledge:**

- <https://www.youtube.com/watch?v=zxQyTK8quyY&t=2053s&pp=ygUWaG93IHRyYW5zZm9ybWVyIG1vZGVscw%3D%3D>
- <https://brev.dev/blog/fine-tuning-llama-2-your-own-data>
- <https://www.youtube.com/watch?v=z2QE12p3kMM>
- <https://huggingface.co/meta-llama/Llama-2-7b-hf>
- <https://blog.google/technology/ai/democratizing-access-to-ai-enabled-coding-with-colab/>
