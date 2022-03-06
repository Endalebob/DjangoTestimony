from django.shortcuts import render, get_object_or_404
from .models import *


def home(request):
    name = "Beloved"
    return render(request, 'home.html', {"name": name})


def story_list(request):
    stories = Story.objects.all()
    stories_with_comment = []
    for story in stories:
        comments = story.comment_set.all()
        if comments:
            number_of_comments = len(comments)
        else:
            number_of_comments = 0
        stories_with_comment.append({"story": story, "number_of_comments": number_of_comments})

    context = {
        "story_list": stories_with_comment
    }
    return render(request, "story_list.html", context)


def comments(request, pk):
    story = get_object_or_404(Story, pk=pk)
    comment = story.comment_set.all()
    if comment:
        context = {
            "book": story,

            "reviews": comment
        }
    else:
        context = {
            "book": story,
            "reviews": None
        }
    return render(request, "comment.html", context)


def story_search(request):
    search_text = request.GET.get("search", "")
    return render(request, "search-results.html", {"search_text": search_text})
