model_name_or_path = "TheBloke/Llama-2-70B-chat-GGML"
model_basename = "llama-2-70b-chat.ggmlv3.q5_1.bin" # the model is in bin format
from huggingface_hub import hf_hub_download
from llama_cpp import Llama
model_path = hf_hub_download(repo_id=model_name_or_path, filename=model_basename)
lcpp_llm = None
lcpp_llm = Llama(
    model_path=model_path,
    n_threads=30, # CPU cores
    n_batch=512, # Should be between 1 and n_ctx, consider the amount of VRAM in your GPU.
    n_gpu_layers=32 # Change this value based on your model and your GPU VRAM pool.
    )
prompt = "Write a linear regression in python"
import os
#from google.colab import drive
#drive.mount('/content/drive')
ll=os.listdir("test-data/judgement/")
#print(ll)
#ff=open("llama_summary/")
for i in range(83,len(ll)):
  counter=0
  lll=open("test-data/judgement/"+ll[i],"r")
  ff=open("llama_summary/"+ll[i],"w")
  lll=lll.read()
  llll=lll.split()
  temp=""
  for j in range(0,len(llll)):
    temp=temp+llll[j]+" "
    counter=counter+1
    if counter % 250 == 0:
      response=lcpp_llm(prompt="You are asked to be a judge of a legal case and provide a judgment of the following legal judgment:-{"+temp+"}", max_tokens=50, temperature=0.7, top_p=0.95,
                  repeat_penalty=1.2, top_k=50,
                  echo=True)
      ttt=response["choices"][0]["text"]
      ttt=ttt.split("}")
      print(ttt[-1])
      ff.write(ttt[-1])
      temp=""
  print("-------------------------------------------------------------")
~                                                                              