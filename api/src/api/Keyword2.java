package api;

public class Keyword2 {
	private String title;
	private String time;
	private String weixinname;
	private String weixinaccount;
	private String weixinsummary;
	private String content;
	private String url;
	private String readnum;
	private String likenum;
	public String getTitle() {
		return title;
	}
	public void setTitle(String title) {
		this.title = title;
	}
	public String getTime() {
		return time;
	}
	public void setTime(String time) {
		this.time = time;
	}
	public String getWeixinname() {
		return weixinname;
	}
	public void setWeixinname(String weixinname) {
		this.weixinname = weixinname;
	}
	public String getWeixinaccount() {
		return weixinaccount;
	}
	public Keyword2(String title, String time, String weixinname, String weixinaccount, String weixinsummary,
			String content, String url, String readnum, String likenum) {
		super();
		this.title = title;
		this.time = time;
		this.weixinname = weixinname;
		this.weixinaccount = weixinaccount;
		this.weixinsummary = weixinsummary;
		this.content = content;
		this.url = url;
		this.readnum = readnum;
		this.likenum = likenum;
	}
	public void setWeixinaccount(String weixinaccount) {
		this.weixinaccount = weixinaccount;
	}
	public String getWeixinsummary() {
		return weixinsummary;
	}
	public void setWeixinsummary(String weixinsummary) {
		this.weixinsummary = weixinsummary;
	}
	public String getContent() {
		return content;
	}
	public void setContent(String content) {
		this.content = content;
	}
	public String getUrl() {
		return url;
	}
	public void setUrl(String url) {
		this.url = url;
	}
	public String getReadnum() {
		return readnum;
	}
	public void setReadnum(String readnum) {
		this.readnum = readnum;
	}
	public String getLikenum() {
		return likenum;
	}
	public void setLikenum(String likenum) {
		this.likenum = likenum;
	}
}
