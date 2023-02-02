package com.ssafy.weather;

public class WeatherDto {
	private String hour;
	private String temp;
	private String wfKor;
	private String wfEn;
	private String reh;
	private String img;

	public WeatherDto() {
		super();
	}

	public String getHour() {
		return hour;
	}

	public void setHour(String hour) {
		this.hour = hour;
	}

	public String getTemp() {
		return temp;
	}

	public void setTemp(String temp) {
		this.temp = temp;
	}

	public String getWfKor() {
		return wfKor;
	}

	public void setWfKor(String wfKor) {
		this.wfKor = wfKor;
	}

	public String getWfEn() {
		return wfEn;
	}

	public void setWfEn(String wfEn) {
		this.wfEn = wfEn;
		this.setImg(wfEn);
	}

	public String getReh() {
		return reh;
	}

	public void setReh(String reh) {
		this.reh = reh;
	}

	public String getImg() {
		return img;
	}

	public void setImg(String wfEn) {
		this.img = wfEn.replace(" ", "_") + ".png";
	}

	@Override
	public String toString() {
		StringBuilder builder = new StringBuilder();
		builder.append("시간: ");
		builder.append(hour + "시");
		builder.append("     ");
		builder.append("온도: ");
		builder.append(temp + "도");
		builder.append("     ");
		builder.append("구름양: ");
		builder.append(wfKor);
		builder.append("     ");
		builder.append("습도: ");
		builder.append(reh + "%");
		return builder.toString();
	}
}
