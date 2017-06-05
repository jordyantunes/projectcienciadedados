package DataScience;

import uk.ac.wlv.sentistrength.*;
import java.sql.*;


public class SentiStrengthApp {
	
	public static String textToSS(String text) {
		return text.trim().replaceAll("\\s+", "+").replaceAll(" ", "+");
    }
	
	public static void main(String args[]){
		Connection c 	= null;
		Statement stmt 	= null;
		PreparedStatement insert_stmt 	= null;
		SentiStrength sentiStrength = new SentiStrength();
		String ssthInitialisation[] = {"sentidata", "/SentStrength_Data/", "scale"};
		sentiStrength.initialise(ssthInitialisation);
		
		try {
			Class.forName("org.sqlite.JDBC");
			c = DriverManager.getConnection("jdbc:sqlite:resources/reviews_2.db");
			c.setAutoCommit(false);
			
			stmt = c.createStatement();
			ResultSet rs = stmt.executeQuery( "SELECT * FROM reviews;" );
			
			int update_count = 0;
			
			while ( rs.next() ) {
				Integer id = rs.getInt("id");
		        String review = rs.getString("review");
		        String[] result_string = sentiStrength.computeSentimentScores(SentiStrengthApp.textToSS(review)).split(" ");
		        Integer result = Integer.parseInt(result_string[0]) + Integer.parseInt(result_string[1]) ; 
		         
		        insert_stmt = c.prepareStatement("UPDATE reviews SET score = ? WHERE id = ?");
		        insert_stmt.setString(1, result.toString());
		        insert_stmt.setString(2, id.toString());
		        
		        insert_stmt.executeUpdate();
		        update_count++;
		    }
			
			c.commit();
			rs.close();
			stmt.close();
		    c.close();
		    
		    System.out.println(update_count + " linhas updated");
			
		} catch (Exception e){
			System.out.println("DEU TRETA");
			System.err.println( e.getClass().getName() + ": " + e.getMessage() );
		    System.exit(0);
		}
	} 
}
