package com.virtualassistant.test;


import org.kie.api.KieServices;
import org.kie.api.runtime.KieContainer;
import org.kie.api.runtime.KieSession;
import org.kie.api.runtime.rule.FactHandle;

public class main {
	public static void main(String[] args) {
		try {
			KieServices ks = KieServices.Factory.get();
			KieContainer kContainer = ks.getKieClasspathContainer();
			KieSession kSession = kContainer.newKieSession("diversion-rule");

			Aeroplane aeroplane =new Aeroplane();
			aeroplane.setFlightName("A01");
			aeroplane.setFuelLevel(40.0F);
			aeroplane.setRequiredLandingDistance(4000);
			FactHandle factHandler;
			kSession.insert(aeroplane);
			kSession.fireAllRules();


			Airport airport =  new Airport();
			airport.setName("paris");
			Runway  runway =  new Runway();
			runway.setName("T1");
			runway.setRunwayDistance(4400);

			Runway runway1 =  new Runway();
			runway1.setName("T2");
			runway1.setRunwayDistance(3800);
			airport.setRunway(runway);

		   kSession.insert(airport);


			System.out.println(aeroplane.getFuelLevel());

		} catch (Exception e) {
			e.printStackTrace();
		}
	}

}

