package api;

public class Keyword {
	private String title;
	private String pubDate;
	private String channelName;
	private String imageurls;
	private String desc;
	private String source;
	private String channelId;
	private String link;
	public Keyword(String title,String pubDate,String channelName,String imageurls,String desc,String source,String channelId,String link){
		this.title = title;
		this.pubDate = pubDate;
		this.channelName = channelName;
		this.imageurls = imageurls;
		this.desc = desc;
		this.source = source;
		this.channelId = channelId;
		this.link = link;
	}
	public String getTitle() {
		return title;
	}
	public void setTitle(String title) {
		this.title = title;
	}
	public String getPubDate() {
		return pubDate;
	}
	public void setPubDate(String pubDate) {
		this.pubDate = pubDate;
	}
	public String getChannelName() {
		return channelName;
	}
	public void setChannelName(String channelName) {
		this.channelName = channelName;
	}
	public String getImageurls() {
		return imageurls;
	}
	public void setImageurls(String imageurls) {
		this.imageurls = imageurls;
	}
	public String getDesc() {
		return desc;
	}
	public void setDesc(String desc) {
		this.desc = desc;
	}
	public String getSource() {
		return source;
	}
	public void setSource(String source) {
		this.source = source;
	}
	public String getChannelId() {
		return channelId;
	}
	public void setChannelId(String channelId) {
		this.channelId = channelId;
	}
	public String getLink() {
		return link;
	}
	public void setLink(String link) {
		this.link = link;
	}
	
	
}
