### All Rights Reserved ###
'''
Developer: Alper Kaan
Date: 17.03.2021
Purpose of Software: question3(HM7)
'''
#Created by InfotechAcademy

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.
'''
Write a program that list according to email addresses without email domains in a text.

Example:

Input:
The advencements in biomarine studies franky@google.com with the investments necessary andDavos sinatra123@.com. Then New Yorker article on wind farms...
yahoo
Output :
franky
sinatra123
'''
import re

txt = "The advencements in biomarine studies franky@google.com with the investments necessary andDavos sinatra123@yahoo.com Then New Yorker article on wind farms..."

email = re.findall(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", txt)


for i in email:
    word = i.split("@")
    print(word[0])

### All Rights Reserved ###

#Copyright (c) ${question3(HM7).2021} ${Alper_Kaan}

#Created by InfotechAcademy

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.

  