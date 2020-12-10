# AutoPPT
this projact can ,using web scraping make a ppt on any topic that is entered.
the code generates a basic ppt using beautiful soup,requests and python-pptx packages.

first I use beautiful soup for scrapping the content from wikipedia.  here, i used the hyperlinks in the beginning of every page as my index. it tells me of all the available topics and hence for each of those topics, the content paragraph is visited. for a start, I picked up the first line each but this might be changable with AI.
I used python-pptx for putting the content in a powerpoint.
this code has been tried and written only in a windows environment. 
though python pptx is a comparitively less developed package, its documentation is available freely:https://python-pptx.readthedocs.io/en/latest/   
this link is for installaton. the same website explains all the other available functons.
one of the biggest problems I faced in pptx was the addition of a second slide. I succeeded when I used a class for a presentation. all the slides are objects.
the following points are what i felt , can be added.
1.add paragraphs of content from wiki
2.add images.(a few more lines of code will allow the addition of images but it will take some logical code to add the images in respective slides instead of adding them all together.)                                                                     
3.add tkinter interface                                                                      
4.remove numbers from the articles.
5. be able to put selective information in the slide. not just the first sentence.
 the code is i python
 i have also attatched a ppt so you can se what it makes, on putting the input as per the jupyter notebook.
                    
