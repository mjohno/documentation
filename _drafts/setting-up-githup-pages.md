---
layout: default
---
# Setting up Github Pages

Surprisingly it took some time setting some of this stuff up. Particularly just reading how to configure Jekyll and serve it out of a Docker container locally. Why write this documentation? I simply want to learn more about, and practise, Docker. As well as recording what I have learnt. For more detail view the source.

## Hypothesis

Since documentation (or anything in a text format) is effectively code, we can apply the same Software Development practices to documentation as we would code.

## Goals

* Practise docker.
* Create a place for my documentation.
* Have a repeatable and easily testable process for producing documentation.

## Method

### 1. Setup [Github Pages](https://pages.github.com/)

Enough said.

### 2. Initialise your index file

Make a file called `index.md` in the root of the repository, committed it and pushed it to github master. A few seconds later it was available at the URL 'https://mjohno.github.io/index.md'.

*Gotcha: At this point in time Github does not know we are going to be using its Jekyll capability to serve the site. As such you have to add the /index.md to the end of your Github Pages url to be able to view it.*

### 3. Setup the Docker build

Create a Dockerfile that installs and runs [Jekyll](https://jekyllrb.com/), and validate that it serves your index.md. It is going to be used to run our local build (and eventually CI). This will help validate that the changes we are making don't break the site.

*Gotcha: Ensure that you are using 0.0.0.0 as your `--host` parameter when running `jekyll serve`. This will allow Docker to route network traffic to the localhost.*

### 4. Choose a theme and config

Jekyll uses `_config.yml` in the root directory of the repository to set the [theme](https://pages.github.com/themes/). Add title, theme and description variables to set them for your site. Since themes are distributed as Ruby Gems, install it before you run jekyll serve. With the `_config.yml` in place Github Pages knows to serve the site using Jekyll.

### 5. Write a draft post

Make a `_drafts` directory and open a file that is going to eventually be a blog post.

*Gotcha: The draft post's name must be hyphen-separated with a .md or .html extension.*

*Gotcha 2: At the top of the post you must have valid yaml [frontmatter](https://jekyllrb.com/docs/frontmatter/) with the `layout` variable set or the theme won't render.*

Add the `--drafts` switch to jekyll serve command in the Dockerfile.
The URL will be available for preview in draft mode at `/year/month/day/name-of-file.html`.

### 6. Setup Travis CI

Activate the repository from within Travis CI. Add a `.travis.yml` file that has the `docker build .` command in it. Create a branch and push to it to watch Travis do its stuff.

## Results

* Fast Feedback with `docker build .` providing a repeatable process.
* Can view changes locally which mostly represents how Github Pages uses Jekyll.

## Future Work

* Set up some kind of linting system, maybe a [spellchecker](https://www.npmjs.com/package/markdown-spellcheck)? 
