import streamlit as st

import google.generativeai as genai
from apikey import google_gemini_api_key,openai_api_key
genai.configure(api_key="AIzaSyDr5hk6x9K618uAfBtgYR3Z9ZvJ4O32yu4")

# from openai import OpenAI
# client= OpenAI(api_key="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")

generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

# SET app to wide mode
st.set_page_config(layout = "wide")
#title of our app
st.title('BlogCraft: Your AI Writing Buddy')

#create a subheader
st.subheader("Now you can craft perfect blogs with the help of AI- BlogCraft is your New AI Blog Companion")

#sidebar for the user input
with st.sidebar:
    st.title("Input your Blog Details")
    st.subheader("Enter Details of the Blog You want to generate")

    #Blog title
    blog_title= st.text_input ("Blog Title")

    #KeyWords input
    keywords = st.text_area("Keywords (comma - separated)")
    #Number of words
    num_words = st.slider(" Number of Words",min_value = 250, max_value = 2000, step = 100)

    # Number of Pages 

    num_images = st.number_input("Number of Images",min_value = 1,max_value =10, step = 1)

    prompt_parts = [
  F"Generate a comprehensive, engaging blog post relevant to the given title \" {blog_title}\" and keywords \"{keywords}\". Make sure to incorporate these keywords in the blog post. The blog should be approximately{num_words}words in length, suitable for an online audience. Ensure the content is original,  informative and maintains a consistent tone throughout. \n**Effects of Generative AI: A Paradigm Shift in Technology and Creation**\n\n**Introduction**\n\nGenerative AI, an emerging field that leverages machine learning to create new and original content, is revolutionizing industries and sparking ethical debates. Its profound effects on creativity, technology innovation, and society as a whole cannot be overstated.\n\n**Artificial Creativity**\n\nGenerative AI models have demonstrated remarkable artistic abilities, generating stunning images, music, and text that rival human creations. This \"artificial creativity\" challenges our traditional notions of originality and authorship. While these models may not possess consciousness or intentionality, they can process vast amounts of data and identify patterns, resulting in surprising and often impressive outcomes.\n\n**Ethical Implications**\n\nThe advent of generative AI raises important ethical questions. Concerns about copyright infringement, job displacement, and the potential for spreading misinformation have been raised. It is crucial to develop ethical guidelines and regulations to ensure that generative AI is used responsibly, respecting human creativity and protecting the integrity of our information landscape.\n\n**Technology Innovation**\n\nGenerative AI is driving significant technological innovation. It has led to the development of novel applications in fields such as:\n\n* **Art and Design:** Creating unique digital art, fashion designs, and interior décor.\n* **Entertainment:** Generating realistic movie special effects, video game characters, and music.\n* **Healthcare:** Identifying drug targets, predicting patient outcomes, and optimizing diagnosis.\n\n**Machine Learning Applications**\n\nGenerative AI operates on powerful machine learning algorithms. By analyzing large datasets, these models learn to generate content that is both coherent and contextually relevant. Notable machine learning applications include:\n\n* **Generative Adversarial Networks (GANs):** Creating realistic images and videos from scratch.\n* **Recurrent Neural Networks (RNNs):** Generating text, code, and music sequences.\n* **Transformer Models:** Translating languages, answering questions, and summarizing text effectively.\n\n**Conclusion**\n\nThe effects of generative AI are far-reaching and transformative. It empowers us to explore uncharted realms of creativity, drives technological advancements, and challenges ethical boundaries. As this technology continues to evolve, it is imperative that we embrace its potential while carefully navigating its implications for society.\n\nGenerative AI poses both opportunities and challenges, prompting us to rethink our understanding of creativity, innovation, and the human experience. By embracing a thoughtful and balanced approach, we can harness the transformative power of this technology for the betterment of both individuals and society as a whole.",
]  
    response = model.generate_content(prompt_parts)
    
    

    
    submit_button = st.button("Generate Blog")

if submit_button:
    # response = model.generate_content(prompt_parts)
    
#     image_response = client.images.generate(
#     model="dall-e-3",
#     prompt="a white siamese cat",
#     size="1024x1024",
#    quality="standard",
#    n=1,
#   )
    # image_url = response.data[0].url

    # st.image(image_url , captions = "Generated Image")

    # st.title("Your Blog Post :")

    st.write(response.text)    


        