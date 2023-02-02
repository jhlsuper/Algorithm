package com.ssafy.weather;

import java.net.URL;
import java.util.ArrayList;
import java.util.List;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;

import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;

public class WeatherDomParser {
	List<WeatherDto> list = new ArrayList<>();

	public List<WeatherDto> getNewsList(String url) {
		list.removeAll(list);
		connectWeather(url);
		return list;

	}

	private void connectWeather(String url) {
		DocumentBuilderFactory f = DocumentBuilderFactory.newInstance();
		try {
			DocumentBuilder parser = f.newDocumentBuilder();
			Document dom = parser.parse(new URL(url).openConnection().getInputStream());
			Element root = dom.getDocumentElement();
			NodeList n = root.getElementsByTagName("data");

			for (int i = 0; i < n.getLength(); i++) {
				WeatherDto w = new WeatherDto();
				Node item = n.item(i);
				NodeList kids = item.getChildNodes();
				for (int j = 0; j < kids.getLength(); j++) {
					Node kid = kids.item(j);
					String name = kid.getNodeName();
					if (name.equalsIgnoreCase("hour")) {
						w.setHour(kid.getFirstChild().getNodeValue());
					} else if (name.equalsIgnoreCase("temp")) {
						w.setTemp(kid.getFirstChild().getNodeValue());
					} else if (name.equalsIgnoreCase("wfKor")) {
						w.setWfKor(kid.getFirstChild().getNodeValue());
					} else if (name.equalsIgnoreCase("wfKEn")) {
						w.setWfEn(kid.getFirstChild().getNodeValue());
					} else if (name.equalsIgnoreCase("reh")) {
						w.setReh(kid.getFirstChild().getNodeValue());
					}
				}
				System.out.println(w);
				list.add(w);
			}
		} catch (Exception e) {
			System.out.println(e);
		}

	}
}