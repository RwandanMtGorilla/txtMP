# Text Mass Production

这是一个使用OpenAI的GPT-3.5-turbo模型进行文本生成的Python脚本。本脚本会根据预设的文本提示生成一段回应，然后将回应存储在本地文件中。可用于同类型文本的批量生成(比如用于学校运动会要求书写大量通讯稿的场景)

## 如何使用

1. **安装必要的Python库：**
   你需要有`requests`和`os`两个Python库。如果没有安装，可以使用以下命令进行安装：
   ```bash
   pip install requests

2. **设置API密钥：**
    你需要将你的OpenAI API密钥填入api_keys列表中。(多个key有助于防止请求失败的情况)例如：

    ```bash
    api_keys = ["your-api-key1", "your-api-key2", "your-api-key3", "your-api-key4"]

3. **运行脚本：**
    在终端中，使用以下命令运行脚本：

    ```bash 
    python main.py

    这将运行脚本并生成回应，然后将回应存储在output目录下的一个txt文件中。

4. **自定义**
    1. 你可以在loop部分修改你希望生成文本的份数
    2. 你可以在脚本中自定义你的文本提示。目前的提示是生成一份运动会的通讯稿。你可以根据需要更改name和project变量，或者直接更改prompt变量来设置你自己的提示。

