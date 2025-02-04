## TikTok Resarch API Query Tool

This is a very basic tool for querying TikTok's research API.

In order to make use of it, you'll need your own credentials stored in a `.env` file that looks like this:

```
CLIENT_ID=<your id>
CLIENT_SECRET=<your secret>
CLIENT_KEY=<your key>
```

And there you go!

### Goals

#### Fields to Pull
These all go in the `fields` parameter in the URL.

* Video ID
* Link (duplicative with ID?)
* Caption
* Hashtags
* User
* Date and Time
* Engagement Stats
* Top 100 Comments?

#### Query Details
We'd like to pull those fields for the top 1k videos (ordered by engagement) that match these criteria, for each year from 2016-2024:

* Tagged with `#adulting`
* In the USA

And then we'll just dump everything to CSV.

#### Open Questions

1. Since we can't order videos, how do we best run these queries? Currently we pull 20 random ones each day.
2. How do we get comments?
