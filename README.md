# Tweet media types

For this project, we'll use the Django [Content Types framekwork](https://docs.djangoproject.com/en/1.10/ref/contrib/contenttypes/) to add different types of tweets to our Twitter clone. Specifically, we'll add **image** and **video** tweets to our regular **text** tweet. We'll need to make our Tweet model support different types of tweet, that should be generic. By "generic" we mean you can't hardcode a `image_url` field to the `Tweet` model. You'll need somehow make use of the model classes `ImageTweet` and `VideoTweet` from `twitter/models.py`. As usual, you'll find out that this process is really simple using the correct Django helper; in this case you might want to take a look at [Generic Relations](https://docs.djangoproject.com/en/1.10/ref/contrib/contenttypes/#generic-relations).

Once you finish implementing your project to support _images_ and _videos_, try extending the project to support a new type of tweet `GistTweet` that receives a Github's Gist URL. If you've used generic relations, it's going to be simple to extend it.

## Base project

As usual, we have our regular Twitter feed view:

![image](https://cloud.githubusercontent.com/assets/872296/18491711/17f32418-79de-11e6-938b-b4660ddc1111.png)

But this time, we'll have the option of creating different type of tweets (_image_, _video_, or the usual _text_ tweet):

![image](https://cloud.githubusercontent.com/assets/872296/18491728/2d01d05c-79de-11e6-988e-0659bcf0d0f6.png)

## Text Tweet

The default type is text:

![image](https://cloud.githubusercontent.com/assets/872296/18491772/6c178084-79de-11e6-9d0a-7d4551a6df6a.png)

## Image Tweet

When you select the "Image Type" a form input will be shown to enter an image URL:

![image](https://cloud.githubusercontent.com/assets/872296/18491812/9af964e4-79de-11e6-9066-0c32726c38a4.png)

When you choose to tweet an image, you should see it in the template:

![image](https://cloud.githubusercontent.com/assets/872296/18491981/6d2b3ff0-79df-11e6-8754-2af60c5dc00d.png)

## Video Tweet

A Video tweet should be created in the same way:

![image](https://cloud.githubusercontent.com/assets/872296/18492057/c233d516-79df-11e6-9a59-8a451be7c667.png)

![image](https://cloud.githubusercontent.com/assets/872296/18492027/9d0813a6-79df-11e6-835b-286001749c05.png)
