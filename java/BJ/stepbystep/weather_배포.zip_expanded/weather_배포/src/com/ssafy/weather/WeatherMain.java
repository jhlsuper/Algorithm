package com.ssafy.weather;

import java.awt.GridLayout;
import java.awt.Image;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;

import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTable;
import javax.swing.SwingConstants;
import javax.swing.table.DefaultTableCellRenderer;
import javax.swing.table.DefaultTableModel;
import javax.swing.table.TableColumnModel;

public class WeatherMain extends JFrame {
	private JPanel northPanel = new JPanel();
	private String[] item = { "서울", "광주", "구미", "대전", "부울경" };
	private String[] dong = { "1168064000", "2915573000", "4719060000", "3020052600", "2635061000" };
	private JComboBox<String> area = new JComboBox<String>(item);
	private JButton b = new JButton("날씨 정보얻기");

	/** 조회 내용 표시할 table */
	private DefaultTableModel tableModel;
	private JTable weatherTable;
	private JScrollPane weatherPan;
	private String[] title = { "아이콘", "시간(시)", "온도(°C)", "날씨", "습도(%)" };

	WeatherSaxParser sax;

	public WeatherMain() {
		super("날씨정보");
		sax = new WeatherSaxParser();
		createGUI();
		addEvent();
	}

	private void createGUI() {
		tableModel = new DefaultTableModel(title, 20);
		weatherTable = new JTable(tableModel) {

			@Override
			public Class<?> getColumnClass(int column) {
				if (getValueAt(0, column) != null)
					return getValueAt(0, column).getClass();
				return String.class;
			}

		};
		weatherTable.setRowHeight(50);
		weatherPan = new JScrollPane(weatherTable);
		weatherTable.setColumnSelectionAllowed(true);

		northPanel.setLayout(new GridLayout(1, 2));
		northPanel.add(area);
		northPanel.add(b);

		add(northPanel, "North");
		add(weatherPan, "Center");
		setSize(600, 500);
		setVisible(true);
	}

	private void addEvent() {
		addWindowListener(new WindowAdapter() {
			public void windowClosing(WindowEvent e) {
				System.exit(0);
			}
		});
		
//		TODO: Lambda 표현식으로 바꾸세요.
		b.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				showList();
			}
		});
	}

	private void showList() {
		int sel = area.getSelectedIndex();
		java.util.List<WeatherDto> datas = sax.getNewsList("http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=" + dong[sel]);
		if (datas != null) {
			int i = 0;
			Object[][] data = new Object[datas.size()][5];
			for (WeatherDto weather : datas) {
				ImageIcon icon = new ImageIcon("img/" + weather.getImg());
				Image image = icon.getImage();
				Image changeImage = image.getScaledInstance(70, 55, Image.SCALE_SMOOTH);
				ImageIcon changeIcon = new ImageIcon(changeImage);
				data[i][0] = changeIcon;
				data[i][1] = weather.getHour();
				data[i][2] = weather.getTemp();
				data[i][3] = weather.getWfKor();
				data[i++][4] = weather.getReh();
			}
			tableModel.setDataVector(data, title);
			tableCellCenter();
		}
	}

	public void tableCellCenter() {
		// 테이블 내용 가운데 정렬하기
		DefaultTableCellRenderer dtcr = new DefaultTableCellRenderer(); // 디폴트테이블셀렌더러를 생성
		dtcr.setHorizontalAlignment(SwingConstants.CENTER); // 렌더러의 가로정렬을 CENTER로

		TableColumnModel tcm = weatherTable.getColumnModel(); // 정렬할 테이블의 컬럼모델을 가져옴

		// 전체 열에 지정
		// for(int i = 0 ; i < tcm.getColumnCount() ; i++){
		// tcm.getColumn(i).setCellRenderer(dtcr);
		// 컬럼모델에서 컬럼의 갯수만큼 컬럼을 가져와 for문을 이용하여
		// 각각의 셀렌더러를 아까 생성한 dtcr에 set해줌
		// }

		// 특정 열에 지정
//		tcm.getColumn(0).setCellRenderer(dtcr);
		tcm.getColumn(1).setCellRenderer(dtcr);
		tcm.getColumn(2).setCellRenderer(dtcr);
		tcm.getColumn(4).setCellRenderer(dtcr);
	}

	public static void main(String[] args) {
		new WeatherMain();
	}

}
